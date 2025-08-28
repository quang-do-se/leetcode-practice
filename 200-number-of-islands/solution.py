from collections import deque
from typing import List

# Slow but accepted solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited_island = set()

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row, col) not in self.visited_island:
                    self.expand_island(grid, row, col)
                    count += 1

        return count

    def expand_island(self, grid, row, col):
        queue = deque()
        queue.append((row, col))
        self.visited_island.add((row, col))

        while len(queue) > 0:
            size = len(queue)

            for _ in range(size):
                current_row, current_col = queue.popleft()

                for direction in self.directions:
                    new_row, new_col = current_row + direction[0], current_col + direction[1]

                    if (new_row, new_col) in self.visited_island:
                        continue

                    if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[row]):
                        continue

                    if grid[new_row][new_col] != "1":
                        continue

                    queue.append((new_row, new_col))
                    self.visited_island.add((new_row, new_col))



sol = Solution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(sol.numIslands(grid))