class Node(object):
    def __init__(self):
        self.val = 0
        self.left = None
        self.right = None

class AVL(object):
    def __init__(self):
        self.root = None

    def getHeight(self, node):
        if node==None: return 0
        return 1+max(self.getHeight(node.left), self.getHeight(node.right))

    def insert(self, value):
        new_node = Node()
        new_node.val = value
        if self.root==None:
            self.root = new_node
            return
        node = self.root
        while node!=None:
            if value < node.val:
                node = node.left
            else:
                node = node.right
        if value < node.val:
            new_node = node.left
        else:
            new_node = node.right
        self.check(new_node)

    def check(self, node):
        # TODO
        return

    def singleRotate(self, node, direction): # -1 = from left, 1 = right
        L = node.left
        R = node.right
        if direction == -1:
            node.left = L.right
            L.right = node
        else:
            node.right = R.left
            R.left = node
        return

    def doubleRotate(self, node, direction):
        L = node.left
        R = node.right
        if direction == -1:
            node.left = self.singleRotate(L, 1)
            return self.singleRotate(node, -1)
        else:
            node.right = self.singleRotate(R, -1)
            return self.singleRotate(node, 1)