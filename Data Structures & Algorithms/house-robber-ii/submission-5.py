class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = nums[0], 0
        dp[1][0], dp[1][1] = nums[0], nums[1]

        # we let dp[i] being the max amount of money robbed so far including i
        for i in range(2, len(nums)):
            dp[i][0] = max(nums[i] + dp[i-2][0], dp[i-1][0])
            dp[i][1] = max(nums[i] + dp[i-2][1], dp[i-1][1])

        return max(dp[len(nums)-2][0], dp[len(nums)-1][1])

        # we have 2 cases: either we rob first house and not last house, or not first house and rob last house
        # so basically just find the max of each rob

        # top down:

        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # memo = [[-1] * 2 for _ in range(len(nums))]

        # def dp(i, start):
        #     # base case
        #     if i == start:
        #         return nums[start]
        #     if i < start:
        #         return 0
        #     if memo[i][start] != -1:
        #         return memo[i][start]
        #     memo[i][start] = max(nums[i] + dp(i-2, start), dp(i-1, start))
        
        #     return memo[i][start]

        # return max(dp(len(nums)-2, 0), dp(len(nums)-1, 1))

