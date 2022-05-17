from django.db import connection
import pika

params = pika.URLParameters(
    "amqps://xkjopces:yoNAN-lWzkBEHN_It-YH9plVSEQANeHN@shark.rmq.cloudamqp.com/xkjopces"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="main", body="hello")
