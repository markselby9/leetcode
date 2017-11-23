# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root: return True
        return abs(self.countHeight(root.left) - self.countHeight(root.right)) <=1 & self.isBalanced(root.left) & self.isBalanced(root.right)

    def countHeight(self, node):
        if not node: return 0
        return 1+max(self.countHeight(node.left), self.countHeight(node.right))

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(0)
# root.right.right = TreeNode(0)
root.left.left = TreeNode(2)
# root.left.left.left = TreeNode(2)
print sol.isBalanced(root)