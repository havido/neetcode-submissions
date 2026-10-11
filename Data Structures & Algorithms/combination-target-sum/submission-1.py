class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # iterate thru each index in the array
        # at each index, backtrack thru each index (so like, )
        # base case: i==len(nums), currSum >= target
        # recursion needs: currsum, currList, currIndex?

        res = []

        def backtrack(currSum, currList, currIndex):
            if currSum >= target:
                if currSum == target:
                    res.append(currList[:])
                return

            for i in range(currIndex, len(nums)):
                currList.append(nums[i])
                backtrack(currSum + nums[i], currList, i)
                currList.pop()
            
        backtrack(0, [], 0)
        return res