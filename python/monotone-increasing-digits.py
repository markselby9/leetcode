class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10: return N
        result = -1
        length = len(str(N))

        for i in range(length - 1, -1, -1):
            digits = [int(x) for x in str(N)]
            if i < length - 1:
                front = int(''.join(str(i) for i in digits[:i + 1])) - 1
                for k in range(len(str(front))):
                    digits[k] = int(str(front)[k])

                for j in range(i + 1, length):
                    digits[j] = 9

            for j in range(i - 1, -1, -1):
                digits[j] = min(digits[j], digits[j + 1])

            print digits
            result = max(result, int(''.join(str(i) for i in digits)))
        return result


print Solution().monotoneIncreasingDigits(332)
print Solution().monotoneIncreasingDigits(12345)
print Solution().monotoneIncreasingDigits(10)
