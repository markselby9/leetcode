__author__ = 'fengchaoyi'


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        str_nums = map(str,nums)
        str_nums = sorted(str_nums, self.compare, reverse=True)
        str_nums = sorted(str_nums, self.compare, reverse=True)
        result = "".join(str_nums).lstrip('0')
        if len(result)==0: return "0"
        return "0" if int(result)==0 else result

    def compare(self, strA, strB):
        return 1 if strA+strB>strB+strA else -1



solution = Solution()
print solution.largestNumber([0])