class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up
        # we let dp[i] be all distinct ways to climb to step i
        dp = [1] * (n+1) # so, at step 0, there is 1 distinct way to climb to step 0

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        # memo = [-1] * n

        # def dp(i):
        #     # base case:
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     if memo[i] != -1:
        #         return memo[i]
            
        #     memo[i] = dp(i+1) + dp(i+2)

        #     return memo[i]
        
        # return dp(0)