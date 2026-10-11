class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # so, if an island hit corner -> is not covered
        # but if we reach the end of recursion without hitting corner -> is fine (i think)

        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        rows, cols = len(board), len(board[0])

        def bfs(r,c):
            queue = deque([(r,c)])
            board[r][c] = "T"
            while queue:
                row,col = queue.popleft()
                for x,y in dir:
                    if 0<=row+x<rows and 0<=col+y<cols and board[row+x][col+y]=="O":
                        queue.append((row+x,col+y))
                        board[row+x][col+y] = "T"

        # bfs from border
        for i in range(cols):
            if board[0][i]=="O":
                bfs(0,i)
            if board[rows-1][i]=="O":
                bfs(rows-1,i)

        for j in range(rows):
            if board[j][0]=="O":
                bfs(j,0)
            if board[j][cols-1]=="O":
                bfs(j, cols-1)
            
        # scan thru rest of board to find regions to color
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="O":
                    board[r][c] = "X"
                elif board[r][c]=="T":
                    board[r][c] = "O"
        



        