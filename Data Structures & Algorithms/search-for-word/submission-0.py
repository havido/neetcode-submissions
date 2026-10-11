class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate til we find first character
        # have a visited list to pass around in recursion, or keep recursion stack manually
        # have a for loop to explore left right up down
        # base case: when word is found, so we can have a pointer to word, when pointer == len: true

        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        row, col = len(board), len(board[0])
        visited = set()
        res = False

        def backtrack(i, r, c):
            # print(i)
            if i == len(word):
                return True
            if r < 0 or r >= row or c < 0 or c >= col or board[r][c] != word[i] or (r,c) in visited:
                return False

            visited.add((r,c))
            for x,y in dir:
                if backtrack(i+1, r+x, c+y):
                    return True
            visited.remove((r,c)) 
            return False

        for r in range(row):
            for c in range(col):
                if backtrack(0, r, c):
                    return True
        return False