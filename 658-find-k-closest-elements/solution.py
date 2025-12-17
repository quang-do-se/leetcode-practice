from typing import List
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        res = []
        i = 0

        for n in arr:
            n_abs = abs(x - n)
            if len(max_heap) < k:
                heapq.heappush(max_heap, -n_abs)
                res.append(n)
            elif n_abs < -max_heap[0]:
                heapq.heappushpop(max_heap, -n_abs)
                i += 1
                res.append(n)

        return res[i:]



sol = Solution()
print(sol.findClosestElements([1,2,3,4,5], 3, 3))
print(sol.findClosestElements([1,1,2,3,4,5], 3, 3))
print(sol.findClosestElements([1,1,1,10,10,10], 1, 9))