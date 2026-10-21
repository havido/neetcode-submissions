class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        max_count = 0
        curr_count = 0
        for c in s:
            if c not in unique:
                unique.add(c)
                curr_count += 1
            else:
                unique = set()
                unique.add(c)
                max_count = max(curr_count, max_count)
                curr_count = 1

        return max_count