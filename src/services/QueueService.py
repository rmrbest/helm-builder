class QueueService(object):

    def __init__(self, QueueStrategy):
        self.strategy = QueueStrategy

    def produce(self, environment, namespace):
        return ""

    def consume(self, environment):
        pass