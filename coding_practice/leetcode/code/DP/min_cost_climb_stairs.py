# https://leetcode.com/problems/min-cost-climbing-stairs/description/
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        prev, cur = cost[0], cost[1]
        for i in xrange(2, len(cost), 1):
            prev, cur = cur, min(prev,cur)+cost[i]
        return min(prev,cur)

