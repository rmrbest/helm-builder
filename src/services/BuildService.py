class BuildService(object):


    def __init__(self, IQueueService):
            self.strategy = IQueueService

    def build(self, environment, namespace):
            pass
