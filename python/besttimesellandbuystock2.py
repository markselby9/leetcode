__author__ = 'fengchaoyi'


class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if (len(prices) <= 1): return 0
        result = 0
        sub_min = prices[0]
        sub_max = prices[0]
        for i in range(len(prices)):
            sub_min = min(prices[i], sub_min)
            sub_max = max(prices[i], sub_max)
            if (i != len(prices) - 1):
                if (prices[i + 1] < prices[i]):
                    result += (sub_max - sub_min)
                    # print (i, sub_max, sub_min, result)
                    sub_min = sub_max = prices[i + 1]
                    # print (i, sub_max, sub_min, result)
            if (i == len(prices) - 1):
                if (prices[i - 1] <= prices[i]):
                    result += (sub_max - sub_min)
                    # print (i, sub_max, sub_min, result)
        return result

# [1,9,6,9,1,7,1,1,5,9,9,9]
print Solution().maxProfit([1, 9, 6, 9, 1, 7, 1, 1, 5, 9, 9, 9])
