class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        length = len(prices)
        leftMaxProfit = [0] * length  # count profit from 0 to i
        rightMaxProfit = [0] * length  # count profit from i to n
        left_min = prices[0]
        right_max = prices[length-1]
        left_max_profit = right_max_profit = 0
        for i in range(length):
            left_min = min(left_min, prices[i])
            left_max_profit = max(prices[i] - left_min, left_max_profit)
            leftMaxProfit[i] = left_max_profit

            right_max = max(right_max, prices[length - i - 1])
            right_max_profit = max(right_max - prices[length - i - 1], right_max_profit)
            rightMaxProfit[length - i - 1] = right_max_profit
        result = 0
        for i in range(length):
            result = max(leftMaxProfit[i]+rightMaxProfit[i], result)
        return result

        # Output Limit Exceeded
        # if len(prices) <= 1: return 0
        # sub_min = prices[0]
        # sub_max = prices[0]
        # best1 = 0
        # best2 = -1
        # for i in range(len(prices)):
        # sub_min = min(prices[i], sub_min)
        # sub_max = max(prices[i], sub_max)
        # if i != len(prices) - 1:
        # if prices[i + 1] < prices[i]:
        #             if sub_max - sub_min > best1:
        #                 best2, best1 = best1, sub_max - sub_min
        #             elif sub_max - sub_min > best2:
        #                 best2 = sub_max - sub_min
        #             sub_min = prices[i + 1]
        #             sub_max = prices[i + 1]
        #     if i == len(prices) - 1:
        #         if prices[i - 1] <= prices[i]:
        #             if sub_max - sub_min > best1:
        #                 best2, best1 = best1, sub_max - sub_min
        #             elif sub_max - sub_min > best2:
        #                 best2 = sub_max - sub_min
        #     print (i, sub_max, sub_min, best1, best2)
        # if best2 == -1: return best1
        # return best1 + best2


print Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0])