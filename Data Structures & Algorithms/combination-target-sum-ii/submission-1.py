class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(currIndex, currSum, currList):
            if currSum == target:
                res.append(currList[:])
                return

            for i in range(currIndex, len(candidates)):
                if i > currIndex and candidates[i] == candidates[i - 1]:
                    continue
                if currSum + candidates[i] > target:
                    return
                currList.append(candidates[i])
                backtrack(i+1, currSum + candidates[i], currList)
                currList.pop()
        
        backtrack(0,0,[])
        return res