class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # no two queens can be on the same row, same col, and (x2-x1)/(y2-y1) has to be ==1 or -1
        # could use set r, set c, set d for O(1) lookup
        # brute force ish: kinda like sudoku: for each queen put down (at each eligible square), recurse on subboard by r & c
        # so only need to check diagonal
        # but there could be 2 subboards, recurse on both of these -> divide & conquer

        # rSet = set()
        cSet = set()
        dSet1 = set()
        dSet2 = set()
        placement = set()  # list of tuples
        res = []

        def backtrack(i):
            print(i)
            if i == n:
                # translate placement to output then append
                output = []
                for num in range(n):
                    currStr = ""
                    for j in range(n):
                        if (num, j) in placement:
                            currStr += "Q"
                        else:
                            currStr += "."
                    output.append(currStr)
                res.append(output)

            for j in range(n):
                # check eligibility
                normalizedD1 = i+j
                normalizedD2 = i-j
                if j not in cSet and normalizedD1 not in dSet1 and normalizedD2 not in dSet2:
                    # rSet.add(i)
                    cSet.add(j)
                    dSet1.add(normalizedD1)
                    dSet2.add(normalizedD2)
                    placement.add((i, j))
                    backtrack(i+1)
                    # rSet.remove(i)
                    cSet.remove(j)
                    dSet1.remove(normalizedD1)
                    dSet2.remove(normalizedD2)
                    placement.remove((i, j))

        backtrack(0)
        return res
