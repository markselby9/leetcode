class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) == 0: return 0
        total_max_profit = 0
        # sub_profit = 0
        sub_min = prices[0]
        for price in prices:
            # if price < 0:
            sub_min = min(sub_min, price)
            total_max_profit = max(price - sub_min, total_max_profit)
        return total_max_profit


print Solution().maxProfit([1, 2, -1, -3, 9, -3, -2, 2, 3, 12])