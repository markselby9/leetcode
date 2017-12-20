class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        length = len(cost)
        record_map = [0 for i in range(length+1)]
        for i in range(length+1):
            if i < 2:
                record_map[i] = cost[i]
                continue
            if i == length:
                record_map[i] = min(record_map[i - 2], record_map[i - 1])
                continue
            record_map[i] = min(record_map[i-2], record_map[i-1]) + cost[i]
        # print record_map
        return record_map[-1]

print Solution().minCostClimbingStairs([10, 15, 20])
print Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])