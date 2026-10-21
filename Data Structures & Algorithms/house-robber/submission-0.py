class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = max(n+dp[i-2], dp[i-1])
        rob1, rob2 = 0, 0 # rob2 is for the prev house was robbed, rob1 is for the other case

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
    
        return rob2