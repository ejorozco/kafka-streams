import faust
import logging
from asyncio import sleep
from datetime import date, datetime
from random import *

# For terminal logging
log = logging.getLogger(__name__)

date_time_format="%d-%m-%Y, %H:%M"

# Object that will hold 
class Transaction(faust.Record):
    transactionId: str
    msg: str
    transactionAmount: 1000

app = faust.App('fraud_app', broker='kafka://localhost:29092')
source_topic = app.topic('source', value_type=Transaction)
destination_topic = app.topic('output', value_type=Transaction)

# PRODUCER
@app.timer(interval=1.0)
async def send_message():
    random_amount = randint(100, 5000)
    random_transactionId = randint(100, 5000)
    await source_topic.send(value=Transaction(transactionId=random_transactionId,msg=f'account 12345 - purchased {random_amount} tacos',transactionAmount=random_amount),)

# RECIEVER and Model execution
# specify the source_topic and destination_topic to the agent
@app.agent(source_topic, sink=[destination_topic])
async def hello(messages):
    async for message in messages:
        if message is not None:
            log.info(message.msg)
            if message.transactionAmount > 2500:
                # the yield keyword is used to send the message to the destination_topic
                yield Transaction(transactionId=message.transactionId,msg=f'FRAUD DETECTED with amount [{message.transactionAmount}]',transactionAmount=message.transactionAmount)
            else:
                # the yield keyword is used to send the message to the destination_topic
                yield Transaction(transactionId=message.transactionId,msg='GOOD TRANSACTION',transactionAmount=message.transactionAmount)

            await sleep(2)
        else:
            log.info('No message received')

# CONSUMER
@app.agent(destination_topic)
async def recieve(messages):
    async for message in messages:
        print(f'Transaction {message.transactionId} decision is : "{message.msg}"')

# Run main function
# Remember yall, use this code as inspiration and not recycle it
# Be creative and use it to build fun and interesting projects!
if __name__ == '__main__':
    app.main()
