from src.vo.results.actionresult import ActionResult
class QueueService(object):

    def __init__(self, QueueStrategy):
        self.strategy = QueueStrategy

    def create_channel(self):
        try:
            self.strategy.create_channel()
        except Exception:
            pass

    def produce(self):
        try:
            self.strategy.produce()
            return ActionResult(True, "Ok")
        except Exception:
            return ActionResult(False, Exception.message)

    def consume(self, environment):
        pass