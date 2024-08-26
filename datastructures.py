import random
import string


class Node:
    def __init__(self, stringLength):
        self.randomString = DataStructuresWork.generateRandomStrings(stringLength)


class ArrayNode(Node):
    pass

class ListNode(Node):
    def __init__(self, stringLength):
        self.next = None
        self.prev = None
        self.spare = None

        super().__init__(stringLength)


class TreeNode(Node):
    def __init__(self, stringLength):
        self.left = None
        self.right = None
        self.spare = None

        super().__init__(stringLength)


class DataStructuresWork:

    def __init__(self):
        print("super init")

    @staticmethod
    def generateRandomStrings(stringLength):
        randomString = ''
        for j in range(stringLength):
            letter = random.choice(string.ascii_letters)
            randomString += letter
        return randomString
