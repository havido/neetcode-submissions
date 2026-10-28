class Solution:
    def climbStairs(self, n: int) -> int:
        # at any step, you have 2 choices to do 1 or 2 steps
        # so worst case: O(2^n)
        # but some of these ways within 2^n steps would overlap
        # so we can do memo table: 
            # at the last step i==n, step==1
            # at the step i==n-2, there's only 1 unique way to climb to top
            # at step i==n-3, there are 2 unique ways: 1+(memo[i+1]+memo[i+2]) ?
            # at step i==n-4, there are 3 unique ways (example): 1+(memo[i+1]+memo[i+2])=3
        
        memo = [-1] * n

        def dp(i):
            # base case:
            if i > n:
                return 0
            if i == n:
                return 1
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = dp(i+1) + dp(i+2)

            return memo[i]
        
        return dp(0)