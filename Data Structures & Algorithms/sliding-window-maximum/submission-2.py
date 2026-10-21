class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # index
        res = []
        l = r = 0

        while r < len(nums):
            # pop right
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
        
            # pop left (expired)
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        
        return res
