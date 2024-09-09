import lists
import trees


class UnitTests:
    def __init__(self, intData):
        self.intData = intData

    @staticmethod
    def calculateNodeData(intData, numberOfNodes):
        return intData * (numberOfNodes - 1)


class ListUnitTests(UnitTests):
    def __init__(self, intData):
        super().__init__(intData)

    def testPushStack(self):
        pass

    def testPopStack(self):
        pass

    def testEnQueue(self):
        pass

    def testDeQueue(self):
        pass


class TreeUnitTests(UnitTests):
    def __init__(self, intData):
        super().__init__(intData)




