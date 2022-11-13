from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c): # BFS function to find the amount of tiles in one island
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            counter = 1
            while q:
                row, col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r<0 or r>=rows or c<0 or c>=cols or grid[r][c] == 0 or (r, c) in visited): continue
                    visited.add((r, c))
                    q.append((r, c))
                    counter += 1
            return counter

        island_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    cur_island = bfs(r, c)
                    if cur_island > island_area:
                        island_area = cur_island
        return island_area

if __name__ == "__main__":

    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    print(Solution().maxAreaOfIsland(grid))
