from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        if image[sr][sc] == color:
            return image

        queue = deque()
        queue.appendleft((sr, sc))
        original_color = image[sr][sc]
        image[sr][sc] = color

        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        while len(queue) > 0:
            queue_size = len(queue)

            for _ in range(queue_size):
                cr, cc = queue.popleft()

                for direction in directions:
                    nr, nc = cr + direction[0], cc + direction[1]

                    if nr < 0 or nr > len(image) - 1 or nc < 0 or nc > len(image[nr]) - 1:
                        continue

                    if image[nr][nc] == original_color:
                        queue.appendleft((nr, nc))
                        image[nr][nc] = color

        return image


sol = Solution()
print(sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(sol.floodFill([[0,0,0],[0,0,0]], 0, 0, 0))
print(sol.floodFill([[0,0,0],[0,0,0]], 1, 1, 1))
