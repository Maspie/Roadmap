class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROW, COL = len(grid), len(grid[0])
        q = deque()
        minute = 0
        fresh = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r,c))

                if grid[r][c] == 1:
                    fresh += 1


        while q and fresh > 0:

            for _ in range(len(q)):
                R,C = q.popleft()

                for dr, dc in directions:
                    r,c = dr + R, dc + C

                    if 0 <= r < ROW and 0 <= c < COL and grid[r][c] == 1:
                        grid[r][c] = 2
                        
                        q.append((r,c))
                        fresh -= 1


            minute += 1
        return minute if fresh == 0 else -1

        