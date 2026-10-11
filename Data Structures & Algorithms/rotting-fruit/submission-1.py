class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # keep time variable - or res
        # multi source bfs

        minutes = 0
        freshCount = 0
        visited = set()
        queue = deque()
        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        rows, cols = len(grid), len(grid[0])

        # precompute all rotten fruit
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    freshCount += 1

        # multisource bfs
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for x,y in dir:
                    if 0<=row+x<rows and 0<=col+y<cols and (row+x,col+y) not in visited and grid[row+x][col+y] == 1:
                        visited.add((row+x,col+y))
                        queue.append((row+x,col+y))
                        freshCount -= 1
            if queue:
                minutes += 1

        return minutes if freshCount == 0 else -1