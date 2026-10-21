class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        i = 1
        while i < len(intervals):
            last_merged = res[-1]
            curr = intervals[i]
            if curr[0] <= last_merged[1]:
                last_merged[1] = max(curr[1], last_merged[1])
            else:
                res.append(curr)

            i += 1
            
        return res
        
