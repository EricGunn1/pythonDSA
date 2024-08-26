from datastructures import DataStructuresWork as DSW
from datastructures import ListNode


class LinkedListWork(DSW):

    def __init__(self, stringLength, numberOfStrings):
        self.head = None
        self.tail = None
        self.stringLength = stringLength
        self.numberOfStrings = numberOfStrings
        self.makeRandomStringLinkedList()
        super().__init__()

    def makeRandomStringLinkedList(self):
        for i in range(self.numberOfStrings):
            node = ListNode(self.stringLength)
            if self.head:   # do we have to make the comparison every time?
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:
                self.head = node
                self.tail = node

    @staticmethod
    def printLinkedList(node):
        print(node.randomString)
        # while ref.next:
            # print(node.randomString)
            # ref = ref.next





