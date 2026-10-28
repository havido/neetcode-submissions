class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # at each step, the cost is cost(currstep) + min(cost(i+1), cost(i+2))
        # so to get mincost, we call cost(0)
        
        memo = [-1] * len(cost)

        def dp(i):
            # base case
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        
        return min(dp(0), dp(1))