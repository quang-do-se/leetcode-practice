from collections import deque
from typing import List


class Solution:
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        m = len(mat)
        n = len(mat[0])

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        step = 0

        while queue:
            queue_size = len(queue)

            for _ in range(queue_size):
                cell_row, cell_col = queue.popleft()

                for dx, dy in self.directions:
                    new_cell_row, new_cell_col = cell_row + dx, cell_col + dy

                    if (
                        0 <= new_cell_row < m
                        and 0 <= new_cell_col < n
                        and (new_cell_row, new_cell_col) not in visited
                    ):
                        queue.append((new_cell_row, new_cell_col))
                        visited.add((new_cell_row, new_cell_col))
                        mat[new_cell_row][new_cell_col] = step + 1

            step += 1

        return mat


sol = Solution()
print(
    sol.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
)
print(
    sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
)
print(
    sol.updateMatrix([[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]])
    == [[0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]
)
