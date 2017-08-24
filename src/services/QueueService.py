class QueueService(object):

    def __init__(self, QueueStrategy):
        self.strategy = QueueStrategy

    def create_channel(self):
        self.strategy.create_channel()

    def produce(self):
        self.strategy.produce()

    def consume(self, environment):
        pass