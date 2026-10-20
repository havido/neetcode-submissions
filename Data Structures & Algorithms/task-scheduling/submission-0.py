class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapq.heapify(maxheap)

        time = 0
        queue = deque() # pairs of [cnt, idleTime]

        while maxheap or queue:
            time += 1

            if not maxheap:
                time = queue[0][1]
            else:
                c = 1 + heapq.heappop(maxheap)
                if c != 0:
                    queue.append([c, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])
            
        return time


