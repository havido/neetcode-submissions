class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(currIndex, currList):
            res.append(currList[:])
            for i in range(currIndex, len(nums)):
                if i > currIndex and nums[i] == nums[i-1]:
                    continue
                currList.append(nums[i])
                backtrack(i + 1, currList) # add
                currList.pop()
                # backtrack(currIndex + 1, currList) # doesn't add
        backtrack(0, [])
        return res