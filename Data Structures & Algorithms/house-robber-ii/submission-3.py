class Solution:
    def rob(self, nums: List[int]) -> int:
        # we have 2 cases: either we rob first house and not last house, or not first house and rob last house
        # so basically just find the max of each rob

        # top down:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dp(i, start, end):
            # base case
            if i == start:
                return nums[start]
            if i < start:
                return 0
            if memo[i][start] != -1:
                return memo[i][start]
            memo[i][start] = max(nums[i] + dp(i-2, start, end), dp(i-1, start, end))
        
            return memo[i][start]

        return max(dp(len(nums)-2, 0, len(nums)-1), dp(len(nums)-1, 1, len(nums)))