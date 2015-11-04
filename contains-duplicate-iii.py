class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if (len(nums)) <= 1: return False
        sorted_nums_pos = sorted(range(len(nums)), key=lambda x:nums[x])
        # nums = sorted(nums)
        i = 0
        while i < len(sorted_nums_pos)-1:
            j=i+1
            # notice
            while j < len(nums) and nums[sorted_nums_pos[j]]-nums[sorted_nums_pos[i]] <= t:
                if abs(sorted_nums_pos[j] - sorted_nums_pos[i]) <= k:
                    return True
                j+=1
            i+=1
        return False

sol = Solution()
print sol.containsNearbyAlmostDuplicate([0, 11, 0], 1, 4)