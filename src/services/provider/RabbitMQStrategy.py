import QueueStrategy
import pika

class RabbitMQStrategy():


    def __init__(self):
        self.connection = None
        self.channel = None
        self.count = 0
        self.connect()

    def create_channel(self):
        pass

    def produce(self):
        self.channel.basic_publish(exchange='',
                              routing_key='hello',
                              body='Hello World!')
        pass

    def connect(self):
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            self.channel = self.connection.channel()
            self.count = self.channel.queue_declare(queue='hello')
        except Exception:
            pass

    def count(self):
        return self.count


