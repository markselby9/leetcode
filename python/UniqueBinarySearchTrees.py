__author__ = 'fengchaoyi'
# n = 3 returns 5

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n==0: return 1
        if n==1: return 1
        result = 0
        for i in range(0, n):
            result += self.numTrees(i)*self.numTrees(n-i-1)
        return result

sol = Solution()
print sol.numTrees(3)
assert (sol.numTrees(3)==5)
print sol.numTrees(11)
