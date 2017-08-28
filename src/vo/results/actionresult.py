class ActionResult(object):

    def __init__(self, success, returnValues=None):
        self.success=success
        self.returnValues = returnValues

    def success(self):
        return self.success

    def getValues(self):
        return self.returnValues