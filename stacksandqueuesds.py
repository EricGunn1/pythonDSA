from datastructures import DataStructuresWork as DSW
from datastructures import ListNode


class Stack(DSW):

    def __init__(self, stringLength, numberOfStrings):
        self.tail = None
        self.stringLength = stringLength
        self.numberOfStrings = numberOfStrings

        super().__init__()

    def makeRandomStringStack(self):
        for i in range(self.numberOfStrings):
            node = ListNode(self.stringLength)
            if self.tail:   # do we have to make the comparison every time?
                node.prev = self.tail
                self.tail = node
            else:
                self.tail = node


class Queue(DSW):

    def __init__(self, stringLength, numberOfStrings):
        self.head = None
        self.stringLength = stringLength
        self.numberOfStrings = numberOfStrings

        super().__init__()

    def makeRandomStringQueue(self):
        for i in range(self.numberOfStrings):
            node = ListNode(self.stringLength)
            node.next = self.head
            if self.head:   # do we have to make the comparison every time?
                while node.next.next:
                    node = node.next.next
                node = node.next
            else:
                self.head = node
