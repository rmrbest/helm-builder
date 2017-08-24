import QueueStrategy
import pika

class RabbitMQStrategy(QueueStrategy):

    def __init__(self, config):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
