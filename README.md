# FICO - MLT Case Study Kafka Demo

## Fraud detection using Kafka Streams/Faust Library

### What is Kafka Streams?
Kafka Streams is a client library for building applications and microservices, where the input and output data are stored in an Apache Kafka® cluster. It combines the simplicity of writing and deploying standard Java and Scala applications on the client side with the benefits of Kafka’s server-side cluster technology.

### What is Faust?
Faust is a stream processing library, porting the ideas from Kafka Streams to Python.

It is used at Robinhood to build high performance distributed systems and real-time data pipelines that process billions of events every day.

### Why use Streams?
Streams allows application recieve and process data in real-time with low latency and high throughput.

### Running sample Faust program 
Prerequisite: Install docker and python3

From the project root, execute this command to initialize Kafka Cluster

```
docker-compose up -d
```

Check cluster health
```
docker ps 
```
```
$ docker ps
CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS          PORTS                                        NAMES
4e149c12be7d   confluentinc/cp-kafka:5.2.0       "/etc/confluent/dock…"   54 minutes ago   Up 8 minutes    9092/tcp, 0.0.0.0:29092->29092/tcp           kafka
4a2b4924dbd6   confluentinc/cp-zookeeper:5.2.0   "/etc/confluent/dock…"   54 minutes ago   Up 54 minutes   2888/tcp, 0.0.0.0:2181->2181/tcp, 3888/tcp   zookeeper
```

Install python3 dependencies
```
python3 -m pip install -U -r requirements.txt
```

note: if issues, please see dependency requirments. May need to downgrade or uninstall dependencies

run application
```
faust -A fraud_app worker -l info
```

### References

https://faust-streaming.github.io/faust/playbooks/quickstart.html
https://github.com/faust-streaming/faust
