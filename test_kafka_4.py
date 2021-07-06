from kafka import KafkaConsumer


def consuer_demo():

    consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))


def main():
    consuer_demo()

main()