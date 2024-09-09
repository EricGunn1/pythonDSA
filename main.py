import lists
import trees
import unittests as ut
import random

if __name__ == '__main__':

    numberOfNodes = 100

    tree = trees.BinarySearchTree()
    tree.buildTree(numberOfNodes)
    rv = tree.breadthFirstSearch()
    print(rv)


