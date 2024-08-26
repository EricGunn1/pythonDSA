
from arrayds import ArrayWork as aw
from linkedlistds import LinkedListWork as llw
from stacksandqueuesds import Stack, Queue


if __name__ == '__main__':
    stringLength = 30
    numberOfStrings = 1

    arrayObj1 = aw(stringLength, numberOfStrings)
    # arrayObj1.printArray()

    ll1 = llw(stringLength, numberOfStrings)
    ll1.printLinkedList(ll1.head)

    stack1 = Stack(stringLength, numberOfStrings)
    stack1.makeRandomStringStack()

    queue1 = Queue(stringLength, numberOfStrings)
    queue1.makeRandomStringQueue()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
