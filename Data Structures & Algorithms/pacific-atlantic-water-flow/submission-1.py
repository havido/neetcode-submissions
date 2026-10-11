class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        res = []
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])

        def dfs(r,c,currSet):
            # reverse the flow
            # if (r,c) in pacific:
            #     return
            # if (r,c) in atlantic:
            #     return

            currSet.add((r,c)) # visited
            
            for x,y in dir:
                if 0<=r+x<rows and 0<=c+y<cols and (r+x,c+y) not in currSet and heights[r+x][c+y] >= heights[r][c]:
                    dfs(r+x,c+y, currSet)
            
        # precompute
        for i in range(cols):
            dfs(0,i,pacific)
            dfs(rows-1, i, atlantic)
        for i in range(rows):
            dfs(i,0,pacific)
            dfs(i, cols-1, atlantic)
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
