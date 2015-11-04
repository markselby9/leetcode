class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        # if len(digits) == 1:
        #     return list(mapping[digits[0]])
        # last_digit = digits[-1]
        # remaining_digit = digits[:-1]
        # return [r+l for r in self.letterCombinations(remaining_digit) for l in mapping[last_digit]]
        result = []
        while len(digits)>0:
            digit = digits[0]
            if len(result)==0:
                result += mapping[digit]
            else:
                temp_result = result
                result = []
                for letter in mapping[digit]:
                    for temp in temp_result:
                        result.append(temp + letter)
            digits = digits[1:]
        return result

solution = Solution()
print solution.letterCombinations('223')