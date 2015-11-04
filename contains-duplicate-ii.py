class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_map = {}
        i = 0
        while i < len(nums):
            num = nums[i]
            if (num in num_map):
                if i-num_map[num] <= k:
                    print i, num_map
                    return True
            num_map[num] = i
            i+=1
        return False

sol = Solution()
print sol.containsNearbyDuplicate([1,2,3,4,5,1], 5)