from kafka import KafkaProducer

def producer_demo():

    producer = KafkaProducer(bootstrap_servers='localhost:9092') #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]

    for i in range(3):
        msg = "msg%d" % i
        msg = msg.encode()
        producer.send('test', msg)
        producer.close()

def main():
    producer_demo()

main()