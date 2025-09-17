from collections import deque
from typing import List


class Solution:
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()

        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    visited.add((row, col))

        step = 0

        while queue:
            queue_size = len(queue)

            for _ in range(queue_size):
                cell_row, cell_col = queue.popleft()

                for direction in self.directions:
                    new_cell_row, new_cell_col = (
                        cell_row + direction[0],
                        cell_col + direction[1],
                    )

                    if (
                        new_cell_row < 0
                        or new_cell_row > len(mat) - 1
                        or new_cell_col < 0
                        or new_cell_col > len(mat[new_cell_row]) - 1
                    ):
                        continue

                    if (new_cell_row, new_cell_col) not in visited:
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
