class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max heap: (element, index)
        maxheap = []
        low = 0
        res = []

        for i in range(len(nums)):
            heapq.heappush(maxheap, [nums[i] * -1, i])

            # preprocessing
            if i < k - 1:
                continue
            
            low = i - k
            while maxheap[0][1] <= low:
                heapq.heappop(maxheap)

            res.append(maxheap[0][0] * -1)

        return res