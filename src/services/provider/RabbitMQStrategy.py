import QueueStrategy
import pika

class RabbitMQStrategy():

    def __init__(self):
        self.connect()

    def create_channel(self):
        pass

    def produce(self):
        pass

    def connect(self):
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()
            channel.queue_declare(queue='hello')
        except Exception:
            pass


