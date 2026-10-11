class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i, currList):
            res.append(currList[:])

            for j in range(i, len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                currList.append(nums[j])
                backtrack(j+1, currList)
                currList.pop()
        
        backtrack(0, [])
        return res