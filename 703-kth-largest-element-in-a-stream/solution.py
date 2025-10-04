from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif self.min_heap[0] < val:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]


""" sol = KthLargest(3, [4, 5, 8, 2])
print(sol.add(3))
print(sol.add(5))
print(sol.add(10))
print(sol.add(9))
print(sol.add(4))

sol = KthLargest(4, [7, 7, 7, 7, 8, 3])
print(sol.add(2))
print(sol.add(10))
print(sol.add(9))
print(sol.add(9)) """


sol = KthLargest(3, [5, -1])
print(sol.add(2))
