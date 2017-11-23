class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # my naive solution
        # nums_map = {}
        # for num in nums:
        #     if num in nums_map:
        #         return True
        #     nums_map[num] = 1
        # return False

        # clever solution
        return len(set(nums)) != len(nums)

sol = Solution()
print sol.containsDuplicate([1,2,3,1])