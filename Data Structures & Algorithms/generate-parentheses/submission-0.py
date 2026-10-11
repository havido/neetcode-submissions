class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open, close, currStr):
            if len(currStr) == n*2:
                res.append("".join(currStr))
                return
            if close < open:
                currStr.append(")")
                backtrack(open, close + 1, currStr)
                currStr.pop()
            if open < n:
                currStr.append("(")
                backtrack(open + 1, close, currStr)
                currStr.pop()
            
        backtrack(0,0,[])

        return res

            
            