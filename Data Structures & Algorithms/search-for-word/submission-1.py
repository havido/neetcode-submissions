class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate til we find first character
        # have a visited list to pass around in recursion, or keep recursion stack manually
        # have a for loop to explore left right up down
        # base case: when word is found, so we can have a pointer to word, when pointer == len: true

        dir = [(-1,0),(1,0),(0,-1),(0,1)]
        row, col = len(board), len(board[0])

        def backtrack(i, r, c, currStr):
            if i == len(word):
                return True
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] == "#" or board[r][c] != word[i]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"
            for x,y in dir:
                if backtrack(i+1, r+x, c+y, currStr):
                    return True
            board[r][c] = temp
        
        for r in range(row):
            for c in range(col):
                if backtrack(0, r, c, []):
                    return True
        
        return False
            