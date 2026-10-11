class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        rows,cols = len(grid), len(grid[0])
        visited = set()
        queue = deque([])

        # pre-find all treasures
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited.add((r,c))
        
        # process each treasure one by one
        while queue:
            r,c = queue.popleft()
            for x,y in dir:
                if 0<=r+x<rows and 0<=c+y<cols and (r+x,c+y) not in visited and grid[r+x][c+y] != -1:
                    visited.add((r+x,c+y))
                    grid[r+x][c+y] = grid[r][c] + 1
                    queue.append((r+x,c+y))
                    

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 0:
        #             visited = set()
        #             visited.add((r,c))
        #             queue = deque([(r,c)])
        #             distance = 0
        #             while queue:
        #                 row,col = queue.popleft()
        #                 distance += 1
        #                 for x,y in dir:
        #                     if 0<=row+x<rows and 0<=col+y<cols and (row+x,col+y) not in visited and grid[row+x][col+y] != 0 and grid[row+x][col+y] != -1:
        #                         queue.append((row+x, col+y))
        #                         visited.add((row+x, col+y))
        #                         grid[row+x][col+y] = min(grid[row+x][col+y], distance)
        
        

