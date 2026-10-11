class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start time (end time) (O(nlogn))
        sortedIntervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        # traverse thru list of intervals
        currStart = sortedIntervals[0][0]
        currEnd = sortedIntervals[0][1]
        res = []
        for start, end in sortedIntervals:
            if start <= currEnd:
                currEnd = max(currEnd, end)
            else:
                res.append([currStart, currEnd])
                currStart = start
                currEnd = end
        res.append([currStart, currEnd])
        return res
                
