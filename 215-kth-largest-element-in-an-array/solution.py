from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for n in nums[k:]:
            if n > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, n)

        return min_heap[0]


sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], 2) == 5)