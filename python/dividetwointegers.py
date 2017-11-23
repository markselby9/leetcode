__author__ = 'fengchaoyi'

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0: return;
        if divisor == 1: return dividend
        symbol = 0
        # need to consider +/-
        if dividend + divisor < dividend:
            divisor = 0 - divisor
            symbol -= 1
        if dividend + divisor < divisor:
            dividend = 0 - dividend
            symbol -= 1
        if dividend == divisor: return -1 if symbol == -1 else 1;

        result = 0

        #consider digital left move
        while dividend >= divisor:
            temp = divisor
            numberof2=0
            while dividend >= temp:
                result += 1 << numberof2
                dividend -= temp;
                temp <<=1
                numberof2 +=1

        # count result one by one is slow
        # while dividend > temp:
        #     result += 1;
        #     temp += divisor;
        return -result if symbol == -1 else -result


sol = Solution()
print sol.divide(2, 2)