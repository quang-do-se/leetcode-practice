from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for pair in points:
            distance = self.get_distance_from_center(pair[0], pair[1])

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, pair))
            elif distance < -max_heap[0][0]:
                heapq.heappushpop(max_heap, (-distance, pair))

        return [pair for (_, pair) in max_heap]

    def get_distance_from_center(self, x: int, y: int):
        return x * x + y * y


sol = Solution()
print(sol.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]])
print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[-2, 4], [3, 3]])