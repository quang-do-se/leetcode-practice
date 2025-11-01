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
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, pair))

        return [t[1] for t in max_heap]

    def get_distance_from_center(self, x: int, y: int):
        return x * x + y * y


sol = Solution()
print(sol.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]])
print(sol.kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[-2, 4], [3, 3]])
print(
    sol.kClosest(
        [
            [-95, 76],
            [17, 7],
            [-55, -58],
            [53, 20],
            [-69, -8],
            [-57, 87],
            [-2, -42],
            [-10, -87],
            [-36, -57],
            [97, -39],
            [97, 49],
        ],
        5,
    )
    == [[-69, -8], [-36, -57], [53, 20], [17, 7], [-2, -42]]
)
