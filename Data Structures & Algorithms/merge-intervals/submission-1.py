class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        
        p = 0
        i = 1

        while i < len(intervals):
            if intervals[i][0] <= intervals[p][1]:
                intervals[p][1] = intervals[i][1]
                del intervals[i]
            else:
                p += 1
                i += 1
            
        return intervals
        
