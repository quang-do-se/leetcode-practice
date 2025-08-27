from collections import deque
from typing import List


# Time Limit Exceeded
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                self.find_door_distance(rooms, row, col)

    def find_door_distance(self, rooms, row, col) -> None:
        if rooms[row][col] == 0 or rooms[row][col] == -1:
            return

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque()
        visited = set()

        queue.append((row, col))
        visited.add((row, col))

        step = 0

        while len(queue) > 0:
            queue_len = len(queue)

            for _ in range(queue_len):
                current_row, current_col = queue.popleft()

                if rooms[current_row][current_col] == 0:
                    rooms[row][col] = step
                    return

                # Add valid neighbors
                for direction in directions:
                    neighbor_row = current_row + direction[0]
                    neighbor_col = current_col + direction[1]

                    if (neighbor_row, neighbor_col) in visited:
                        continue
                    if neighbor_row < 0 or neighbor_row > len(rooms) - 1:
                        continue
                    if neighbor_col < 0 or neighbor_col > len(rooms[current_row]) - 1:
                        continue

                    neighbor_cell = rooms[neighbor_row][neighbor_col]

                    if neighbor_cell == -1:
                        continue

                    visited.add((neighbor_row, neighbor_col))
                    queue.append((neighbor_row, neighbor_col))

            step += 1


sol = Solution()
room = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
sol.wallsAndGates(room)
print(room)
