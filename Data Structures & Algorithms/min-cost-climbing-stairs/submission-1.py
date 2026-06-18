class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        prev1 = cost[0]
        prev2 = cost[1]

        for i in range(2,n):
            cur = min(prev1 , prev2) + cost[i]
            prev1 = prev2
            prev2 = cur

        return min(prev1,prev2)
        