class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        visited = set()
        def dfs(r, c, i):

            if i == len(word):
                return True

            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or word[i] != board[r][c]:
                return False

            
            visited.add((r,c))

            movement = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))

            

            visited.remove((r,c))

            return movement



        for row in range(rows):
            for col in range(cols):

                if dfs(row, col, 0):
                    return True
        return False

        
        