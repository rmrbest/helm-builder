# test_QueueService.py
import pytest
import mock
from src.services.QueueService import QueueService
from src.services.provider.FakeQueueStrategy import FakeQueueStrategy
from src.vo.results.actionresult import ActionResult

def test_produce_actionresult_true(mocker):
    queueService = QueueService(FakeQueueStrategy)
    mocker.patch.object(queueService, 'produce')
    queueService.produce.return_value = ActionResult(True, "Ok")
    assert isinstance(queueService.produce(), ActionResult)
    assert queueService.produce().success == True