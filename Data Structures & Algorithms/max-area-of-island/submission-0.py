class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        maxCount = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    currMax = 1
                    queue = deque([(r,c)])
                    grid[r][c] = 0
                    while queue:
                        row, col = queue.popleft()
                        for x,y in dir:
                            if 0 <= row+x < rows and 0 <= col+y < cols and grid[row+x][col+y] == 1:
                                currMax += 1
                                queue.append((row+x, col+y))
                                grid[row+x][col+y] = 0
                    maxCount = max(maxCount, currMax)
        
        return maxCount