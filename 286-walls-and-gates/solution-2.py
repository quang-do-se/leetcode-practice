from collections import deque
from typing import List

# Optimized
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        EMPTY = 2147483647
        DOOR = 0

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque()

        # Search from all DOORs at the same time
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == DOOR:
                    queue.append((row, col))

        while len(queue) > 0:
            queue_len = len(queue)

            for _ in range(queue_len):
                current_row, current_col = queue.popleft()

                # Add valid neighbors
                for direction in directions:
                    neighbor_row = current_row + direction[0]
                    neighbor_col = current_col + direction[1]

                    if neighbor_row < 0 or neighbor_row > len(rooms) - 1:
                        continue
                    if neighbor_col < 0 or neighbor_col > len(rooms[current_row]) - 1:
                        continue

                    if rooms[neighbor_row][neighbor_col] != EMPTY:
                        continue

                    rooms[neighbor_row][neighbor_col] = rooms[current_row][current_col] + 1

                    queue.append((neighbor_row, neighbor_col))


sol = Solution()
room = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
sol.wallsAndGates(room)
print(room)
