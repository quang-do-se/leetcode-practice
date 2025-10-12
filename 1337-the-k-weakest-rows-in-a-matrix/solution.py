from typing import List
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        max_heap = []

        for row in range(len(mat)):
            soldier_count = 0
            for col in mat[row]:
                if col == 1:
                    soldier_count += 1
                else:
                    break

            strength = (-soldier_count, -row)

            if len(max_heap) < k:
                heapq.heappush(max_heap, strength)
            elif strength > max_heap[0]:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, strength)

        res = []
        while len(max_heap) > 0:
            res.append(-heapq.heappop(max_heap)[1])

        res.reverse()

        return res


mat = [
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1],
]

sol = Solution()
print(sol.kWeakestRows(mat, 3))
