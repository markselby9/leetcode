class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        length = len(nums)
        if length == 0: return []
        last_num = nums[0]
        if length == 1: return [str(last_num)]
        answer = []
        
        lower_b = nums[0]
        upper_b = nums[0]
        for i in nums[1:]:
            if i - last_num ==1:
                upper_b = i
            else:
                if upper_b - lower_b == 0:
                    answer.append(str(upper_b))
                else:
                    answer.append(str(lower_b)+"->"+str(upper_b))
                lower_b = i
                upper_b = i
            last_num = i
        if lower_b == last_num:
            answer.append(str(lower_b))
        else:
            answer.append(str(lower_b)+"->"+str(upper_b))
        return answer

sol = Solution()
print sol.summaryRanges([1,2,3,5,6,7,8,9])