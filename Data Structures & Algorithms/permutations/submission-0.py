class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # set to pass the existing nums around with each path
        res = []

        def backtrack(hashset, currList):
            if len(currList) == len(nums):
                res.append(currList[:])
                return
            for num in nums:
                if num in hashset:
                    continue
                hashset.add(num)
                currList.append(num)
                backtrack(hashset, currList)
                currList.pop()
                hashset.remove(num)
        backtrack(set(), [])
        return res