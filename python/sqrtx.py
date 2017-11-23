class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1: return 1
        return self.search(0, x, x)

    def search(self, low, high, x):
        if high==low: return low
        midium = low + (high-low)/2
        mid2 = midium*midium
        if mid2 == x: return midium
        if high-low == 1: return low
        if mid2 > x: return self.search(low, midium, x)
        else: return self.search(midium, high, x)

sol = Solution()
print sol.mySqrt(7)