import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_allocations = []  # We'll use heapq to treat this as a min-heap.
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            # If this is actually a "jump down", skip it.
            if climb <= 0:
                continue
            # Otherwise, allocate a ladder for this climb.
            heapq.heappush(ladder_allocations, climb)
            # If we haven't gone over the number of ladders, nothing else to do.
            if len(ladder_allocations) <= ladders:
                continue
            # Otherwise, we will need to take a climb out of ladder_allocations
            bricks -= heapq.heappop(ladder_allocations)
            # If this caused bricks to go negative, we can't get to i + 1
            if bricks < 0:
                return i
        # If we got to here, this means we had enough to cover every climb.
        return len(heights) - 1


sol = Solution()
print(sol.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4)
print(sol.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7)
print(sol.furthestBuilding([14, 3, 19, 3], 17, 0) == 3)
print(sol.furthestBuilding([1, 1, 6, 3, 11, 19, 25], 6, 2) == 5)
print(sol.furthestBuilding([1, 1, 6, 3, 11, 19, 25], 0, 0) == 1)
print(sol.furthestBuilding([7, 6, 5, 4, 3, 2, 1], 0, 0) == 6)
print(sol.furthestBuilding([1], 0, 0) == 0)
