class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        while len(maxheap) >= 2:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            if x > y:
                x = x - y
                heapq.heappush(maxheap, -x)
            elif y > x:
                y = y - x
                heapq.heappush(maxheap, -y)
        
        return -maxheap[0]