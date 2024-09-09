class ListNode:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class Lists:
    def __init__(self):
        self.head = None


class Stack(Lists):
    def __init__(self):
        super().__init__()

    def pushStack(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

        return self.head, node.next

    def popStack(self):
        if not self.head:
            pass
        else:
            ref = self.head
            self.head = self.head.next
            del ref

        return self.head

    def printStack(self):
        ref = self.head
        while ref.next:
            print(ref.data)
            ref = ref.next
        print(ref.data)


class Queue(Lists):
    def __init__(self):
        self.tail = None
        super().__init__()

    def enQueue(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        return self.head, node.next

    def deQueue(self):
        if not self.tail:
            pass
        else:
            ref = self.tail
            self.tail = self.tail.prev
            del ref

        return self.tail


class LinkedList(Lists):
    def __init__(self):
        super().__init__()
