class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        # for loop for each item in each mapping
        # recursion would be the next digit
        # base case: when len(s) == len(digits)

        if len(digits) == 0:
            return []
        currStr = []
        res = []

        def backtrack(i):
            if len(currStr) == len(digits):
                res.append("".join(currStr))
                return
            
            for j in mapping[digits[i]]:
                currStr.append(j)
                backtrack(i+1)
                currStr.pop()
        backtrack(0)
        return res