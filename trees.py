import random
import collections

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _addNode(self, node, root):
        if not root:
            return node

        if node.data <= root.data:
            root.left = self._addNode(node, root.left)
        elif node.data > root.data:
            root.right = self._addNode(node, root.right)

        return root

    def addNode(self, node):
        if not self.root:
            self.root = node
            return
        else:
            self._addNode(node, self.root)

    def buildTree(self, numberOfNodes):
        for i in range(numberOfNodes):
            node = TreeNode(random.randint(-100,100))
            print(node.data)
            self.addNode(node)

    # don't worry about a func or rv for now
    def breadthFirstSearch(self):
        if not self.root:
            return []

        rv = []
        queue = collections.deque([self.root])

        while queue:
            levelSize = len(queue)
            currentLevel = []
            for i in range(levelSize):
                node = queue.popleft()
                if type(node) == str:
                    currentLevel.append(node)
                else:
                    currentLevel.append(node.data)
                    if node.left:
                        queue.append(node.left)
                    else:
                        queue.append("None")
                    if node.right:
                        queue.append(node.right)
                    else:
                        queue.append("None")
            rv.append(currentLevel)

        return rv

    def inOrderTraversal(self, root):
        if not root:
            return

        self.inOrderTraversal(root.left)
        print(root.data)
        self.inOrderTraversal(root.right)


