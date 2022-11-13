from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == "0" or (r, c) in visited): continue
                    visited.add((r, c))
                    q.append((r, c))

        num_of_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_of_islands += 1
        return num_of_islands

if __name__ == "__main__":

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    
    print(Solution().numIslands(grid))