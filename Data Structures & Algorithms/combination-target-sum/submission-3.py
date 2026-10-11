class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # iterate thru each index in the array
        # at each index, backtrack thru each index (so like, )
        # base case: i==len(nums), currSum >= target
        # recursion needs: currsum, currList, currIndex?

        res = []
        nums.sort()

        def backtrack(currIndex, currSum, currList):
            if currSum == target:
                res.append(currList[:])
                return
            
            for i in range(currIndex, len(nums)):
                if currSum + nums[i] > target:
                    return
                currList.append(nums[i])
                backtrack(i, currSum + nums[i], currList)
                currList.pop()
            
        backtrack(0, 0, [])
        return res