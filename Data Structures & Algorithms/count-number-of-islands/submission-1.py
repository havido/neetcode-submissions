class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        rows, cols = len(grid), len(grid[0])
        count = 0
    
        # # dfs
        # def dfs(r, c):
        #     # base case
        #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '#' or grid[r][c] == '0':
        #         return
        #     grid[r][c] = '#'
        #     for x, y in dir:
        #         dfs(r+x, c+y)
            
        # for r in range(rows):
        #     for c in range(cols):
        #         print(count)
        #         if grid[r][c] == '1':
        #             count += 1
        #             dfs(r,c)

        #==========

        # bfs
        # queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    queue = deque([(r,c)])
                    grid[r][c] = '#'
                    count += 1
                    while queue:
                        row, col = queue.popleft()
                        for x,y in dir:
                            if 0 <= row+x < rows and 0 <= col+y < cols and grid[row+x][col+y] == '1':
                                queue.append((row+x, col+y))
                                grid[row+x][col+y] = '#'


        return count