class Solution:
    def rob(self, nums: List[int]) -> int:
        # memoization?
        # dp = max(n + rob(n-2), rob(n-1))
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums: List[int]) -> int:
            memo = [-1] * len(nums)
            def helper(i) -> int:
                if i >= len(nums):
                    return 0
                if memo[i] != -1:
                    return memo[i]
                memo[i] = max(nums[i] + helper(i+2), helper(i+1))
            
                return memo[i]
            return helper(0)

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))