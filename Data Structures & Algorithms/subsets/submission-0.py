class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for each number, can either appear or not
        # so recurse thru the array, carrying index (base case == len), either add or don't add, recurse to next index
        res = []
        def backtrack(i, currList):
            # base case
            if i == len(nums):
                res.append(currList)
                return
            
            backtrack(i+1, currList) # doesn't add
            backtrack(i+1, currList + [nums[i]]) # add

        backtrack(0, [])
        return res