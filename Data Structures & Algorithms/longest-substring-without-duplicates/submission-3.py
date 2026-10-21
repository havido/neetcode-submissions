class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = {}
        max_count = 0
        left = 0

        for right in range(len(s)):
            if s[right] in unique:
                left = max(unique[s[right]] + 1, left)
            
            unique[s[right]] = right
            max_count = max(right-left+1, max_count)

        return max_count