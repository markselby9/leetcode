__author__ = 'fengchaoyi'
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        self.levelOrderLevel(root, 0, result)
        return result

    def levelOrderLevel(self, node, level, result):
        if node == None:
            return
        else:
            if len(result) <= level:
                result.append([node.val])
            else:
                result[level].append(node.val)
        if node.left != None:
            self.levelOrderLevel(node.left, level+1, result)
        if node.right != None:
            self.levelOrderLevel(node.right, level+1, result)

sol = Solution()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
root.left=node1
root.right=node2
node2.left = node3
node2.right=node4
print sol.levelOrder(root)