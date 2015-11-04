class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit_counter = [~0, 0, 0]
        # bit_counter[1]: bits that appeared 1 time; [2]:appear 2 time
        len_nums = len(nums)
        len_counter = len(bit_counter)
        for i in range(len_nums):
            temp = bit_counter[-1]
            for j in range(len_counter-1, 0, -1):
                bit_counter[j] = (bit_counter[j-1] & nums[i]) | (bit_counter[j] & ~nums[i])
            bit_counter[0] = (temp & nums[i]) | (bit_counter[0] & ~nums[i])
            print i, nums[i], bit_counter
        return bit_counter[1]


sol = Solution()
print sol.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
print sol.singleNumber([2,2,3,2])