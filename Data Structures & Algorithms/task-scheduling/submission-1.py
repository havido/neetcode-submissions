class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tuple: (Task : freq)
        # ^ iterate thru tasks to have those tuple, perhaps could store into map for O(1) access
        # put into queue, ordering by most frequent task queue tip
        
        # preprocessing  
        task_freq = defaultdict(int)
        for t in tasks:
            task_freq[t] += 1

        max_heap = [-f for _, f in task_freq.items()]

        time = 0
        heapq.heapify(max_heap)
        queue = deque()

        while max_heap or queue:
            time += 1
            if not max_heap:
                time = queue[0][1] 
            else:
                count = 1 + heapq.heappop(max_heap)
                if count != 0:
                    queue.append([count, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(max_heap, queue.popleft()[0])
        return time


