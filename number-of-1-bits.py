class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        result = 0
        while n>0:
            result += n % 2
            n = n / 2
        return result

sol = Solution()
print sol.hammingWeight(11)