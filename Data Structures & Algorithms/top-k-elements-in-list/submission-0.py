class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # initialize count map
        count = {}
        # initialize the freq[] bucket
        freq = [[] for i in range(len(nums)+1)]

        # popularize count map for each num in nums
        for num in nums: # O(n)
            count[num] = count.get(num, 0) + 1
        # popularize freq[] bucket
        for num, c in count.items():
            freq[c].append(num)

        res = []
        # traverse thru freq[] bucket from n to 1 to print numbers
        for i in range(len(freq)-1, 1, -1):
            for item in freq[i]:
                res.append(item)
                if len(res) == k:
                    return res
        