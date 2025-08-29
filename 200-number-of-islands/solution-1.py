from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        count = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count += 1
                    queue = []
                    queue.append((row, col))
                    grid[row][col] = "0"

                    while queue:
                        current_row, current_col = queue.pop(0)

                        for direction in directions:
                            new_row, new_col = (
                                current_row + direction[0],
                                current_col + direction[1],
                            )

                            if (
                                new_row < 0
                                or new_row >= len(grid)
                                or new_col < 0
                                or new_col >= len(grid[row])
                            ):
                                continue

                            if grid[new_row][new_col] != "1":
                                continue

                            queue.append((new_row, new_col))
                            grid[new_row][new_col] = "0"

        return count


sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(sol.numIslands(grid))
