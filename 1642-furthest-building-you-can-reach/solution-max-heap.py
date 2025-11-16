import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        max_heap = []

        n = len(heights)

        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]

            if diff < 0:
                continue

            heapq.heappush(max_heap, -diff)
            bricks -= diff

            if bricks < 0:
                biggest_brick_allocation = -heapq.heappop(max_heap)
                if ladders > 0:
                    ladders -= 1
                    bricks += biggest_brick_allocation
                else:
                    return i

        return n - 1


sol = Solution()
print(sol.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4)
print(sol.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7)
print(sol.furthestBuilding([14, 3, 19, 3], 17, 0) == 3)
print(sol.furthestBuilding([1, 1, 6, 3, 11, 19, 25], 6, 2) == 5)
print(sol.furthestBuilding([1, 1, 6, 3, 11, 19, 25], 0, 0) == 1)
print(sol.furthestBuilding([7, 6, 5, 4, 3, 2, 1], 0, 0) == 6)
print(sol.furthestBuilding([1], 0, 0) == 0)
