from kafka import KafkaConsumer

consumer = KafkaConsumer('pdd_kafka', bootstrap_servers=['localhost:9092'])
for msg in consumer:
    recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
    print(recv)