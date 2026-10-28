class Solution:
    def rob(self, nums: List[int]) -> int:
        # top down
        # observation: at each house, we can choose to rob or not rob the house
            # if rob: result = curr house + max(house-2)
            # if not rob: result = max(house-1)
        # so, dp = max(currhouse + rob(house-2), rob(house-1))

        memo = [-1] * len(nums)

        def dp(n):
            # base case
            if n < 0:
                return 0
            if n == 0:
                return nums[n]
            if memo[n] != -1:
                return memo[n]
            memo[n] = max(nums[n] + dp(n-2), dp(n-1))
            return memo[n]
        return dp(len(nums) - 1)