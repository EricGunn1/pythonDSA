import random
import string
from datastructures import DataStructuresWork as DSW

# this class should not initialize an array, it should just be algorithms for working on arrays
class ArrayWork(DSW):

    def __init__(self, stringLength, numberOfStrings):
        self.randomStringList = []
        for i in range(numberOfStrings):
            stringData = DSW.generateRandomStrings(stringLength)
            self.randomStringList.append(stringData)

        super().__init__()

    def printArray(self):
        for item in self.randomStringList:
            print(item)
