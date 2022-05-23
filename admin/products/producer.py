import pika
import json

params = pika.URLParameters(
    "amqps://xkjopces:yoNAN-lWzkBEHN_It-YH9plVSEQANeHN@shark.rmq.cloudamqp.com/xkjopces"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="", routing_key="main", body=json.dumps(body), properties=properties
    )
