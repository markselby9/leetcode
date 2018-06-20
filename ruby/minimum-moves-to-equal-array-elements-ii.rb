# @param {Integer[]} nums
# @return {Integer}
def min_moves2(nums)
	nums.sort!

	p1 = 0
	p2 = nums.length - 1
	result = 0
	while p1 <= p2 do
		result += nums[p2] - nums[p1]
		p1 += 1
		p2 -= 1
	end
	result
end