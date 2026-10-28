class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        # observation: at each house, we can choose to rob or not rob the house
            # if rob: result = curr house + max(house-2)
            # if not rob: result = max(house-1)
        # so, dp = max(currhouse + rob(house-2), rob(house-1))

        # memo = [-1] * len(nums)

        # def dp(n):
        #     # base case
        #     if n < 0:
        #         return 0
        #     if n == 0:
        #         return nums[n]
        #     if memo[n] != -1:
        #         return memo[n]
        #     memo[n] = max(nums[n] + dp(n-2), dp(n-1))
        #     return memo[n]
        # return dp(len(nums) - 1)

        # bottom up
        # we let dp[i] be the max profit up until ith house (including)

        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * (n) 
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        return dp[n-1]
