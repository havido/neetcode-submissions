class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    queue = deque([(i,j)])
                    grid[i][j] = "X"
                    count += 1

                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in dirs:
                            if 0<=x+dx<rows and 0<=y+dy<cols and grid[x+dx][y+dy] == "1":
                                queue.append([x+dx, y+dy])
                                grid[x+dx][y+dy] = "X"
        return count            