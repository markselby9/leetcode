# @param {String} s
# @param {Integer[]} shifts
# @return {String}
def shifting_letters(s, shifts)
	move = 0
	result = []
	s = s.chars
	for i in 0..shifts.length-1
		i = shifts.length - 1 - i
		move += shifts[i]
		move %= 26
		result.push(('a'.ord + (s[i].ord - 'a'.ord + move) % 26).chr)
	end
	print result
	result.reverse.join()
end

S = "abc", shifts = [3,5,9]
print shifting_letters("abc", [3,5,9])