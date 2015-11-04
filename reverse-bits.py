class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_str = bin(n)
        reversed_bin_str = bin_str[-1:1:-1]+'0'*(32-len(bin_str)+2)
        print bin_str, reversed_bin_str
        return long(reversed_bin_str, base = 2)

sol = Solution()
print sol.reverseBits(43261596)