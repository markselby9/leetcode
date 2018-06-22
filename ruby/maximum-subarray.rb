# @param {Integer[]} nums
# @return {Integer}
def max_sub_array(nums)
	length = nums.length
	if length == 0
		return 0
	end
	if length == 1
		return nums[0]
	end
	current_max = -9999999
	temp = 0
	local = 0
	(0..length-1).each do |i|
		local += nums[i]
		current_max = [current_max, local].max
		temp += nums[i]
		if temp < 0
			temp = 0
			local = 0
		end
	end
	current_max
end


print max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
print max_sub_array([-2, -1, -3])
print max_sub_array([-2, -1, -3, 4, -3])