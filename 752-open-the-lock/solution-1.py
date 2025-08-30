from collections import deque
from typing import List


# Optimized
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        lock = (0, 0, 0, 0)
        target_lock = tuple(int(e) for e in target)

        visited = set()
        queue = deque()

        for deadend in deadends:
            visited.add(tuple(int(e) for e in deadend))
        
        if lock in visited:
            return -1

        visited.add(lock)        
        queue.append(lock)
        step = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                current_lock = queue.popleft()

                if current_lock == target_lock:
                    return step

                for i in range(4):
                    for addition in [1, -1]:
                        temp_lock = list(current_lock)
                        temp_lock[i] = (current_lock[i] + addition) % 10

                        new_lock = tuple(temp_lock)

                        if new_lock not in visited:
                            queue.append(new_lock)
                            visited.add(new_lock)
            step += 1

        return -1


sol = Solution()
print(sol.openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6)
print(sol.openLock(["8888"], "0009") == 1)
print(
    sol.openLock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    ) == -1
)
print(sol.openLock(["0000"], "8888") == -1)
