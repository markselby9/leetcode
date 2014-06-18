# the dumb way of simply max - prices[0] would cause TLE
# better way is to deal with the array first and then compute the largest segment sum, tricky!
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        result = 0
	size = len(prices)
	if size < 1: return 0
	for i in range(size-1):
	    prices[i] = prices[i+1]-prices[i]
	prices[size-1] = 0
        segsum = 0
	for i in range(size):
	    segsum += prices[i]
	    if segsum < 0: segsum = 0
	    if result < segsum: result = segsum
	return result

prices = [7,-3,4,0,1,2,3,4,5,6,7]
c = Solution()
print c.maxProfit(prices)	
