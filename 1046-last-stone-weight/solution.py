from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            bigger = -heapq.heappop(max_heap)
            smaller = -heapq.heappop(max_heap)

            if bigger > smaller:
                heapq.heappush(max_heap, smaller - bigger)

        return -max_heap[0] if max_heap else 0


sol = Solution()
print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1)
print(sol.lastStoneWeight([1]) == 1)
print(sol.lastStoneWeight([1, 4]) == 3)
print(sol.lastStoneWeight([2, 2]) == 0)
