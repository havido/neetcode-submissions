class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up
        # we let dp[i] be all distinct ways to climb to step i
        dp = [0] * (n+1) # so, at step 0, there is 1 distinct way to climb to step 0
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]