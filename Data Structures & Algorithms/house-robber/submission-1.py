class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp = max(n + dp(n-2), dp(n-1))
        # rob1 is prev house was skipped, rob2 is prev house was robbed
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
