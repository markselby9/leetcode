# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def search_range(nums, target)
	res = search_num(target, nums)
	if res == -1
		return [-1, -1]
	end

	t1 = res
	left, right = 0,0
	t2 = -1
	while t1!=t2 do
		t2 = search_num(target, nums[0..t1])
		if t2==-1
			break
		end
		t1 = search_num(target, nums[0..t2])
	end
	if t2!=-1
		left = t2
	else
		left = res
	end

	right = res
	t = search_num(target, nums[right+1..nums.length+1])
	while t!=-1
		right = t + right + 1
		t = search_num(target, nums[right+1..nums.length+1])
	end

	[left, right]
end

def search_num(number, array)
	if array.length === 0
		-1
	end
	l, r = 0, array.length - 1
	while l < r do
		m = (l + r) / 2
		if number == array[m]
			return m
		end
		if number > array[m]
			l = m + 1
		else
			r = m
		end
	end
	if array[l] == number
		return l
	end
	if array[r] == number
		return r
	end
	-1
end

print search_num(5, [1,3,3,3,3,5])
nums = [5,7,7,8,8,10]
target = 8
print search_range(nums, target)
nums = [5,7,7,8,8,10]
target = 6
print search_range(nums, target)
print search_range([2,2], 2)
print search_range([2,2,2,2,2], 2)