from typing import List
import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_heap = sticks
        heapq.heapify(min_heap)

        cost = 0

        while len(min_heap) > 1:
            first = heapq.heappop(min_heap)
            second = heapq.heappop(min_heap)
            new_stick = first + second
            cost += new_stick
            heapq.heappush(min_heap, new_stick)

        return cost
    
sol = Solution()
print(sol.connectSticks([2,4,3]))
print(sol.connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009]))