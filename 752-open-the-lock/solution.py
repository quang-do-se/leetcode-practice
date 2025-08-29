from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        lock = (0, 0, 0, 0)
        target_lock = tuple(int(e) for e in target)
        deadend_locks = set()
        for deadend in deadends:
            deadend_locks.add(tuple(int(e) for e in deadend))

        if lock in deadend_locks:
            return -1

        visited = set()
        queue = deque()

        queue.append(lock)
        visited.add(lock)
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

                        if new_lock not in visited and new_lock not in deadend_locks:
                            queue.append(new_lock)
                            visited.add(new_lock)
            step += 1

        return -1


sol = Solution()
print(sol.openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
print(sol.openLock(["8888"], "0009"))
print(
    sol.openLock(
        ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"
    )
)
print(sol.openLock(["0000"], "8888"))
