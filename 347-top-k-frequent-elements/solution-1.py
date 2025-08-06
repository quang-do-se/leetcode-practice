from typing import List
import heapq

# Sort solution - O(nlog(n))
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        
        sorted_frequency = sorted(frequency.items(), key=lambda kv: (-kv[1], kv[0]))

        res = []
        for i in range(k):
            res.append(sorted_frequency[i][0])
        
        return res


sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([-1, -1], 1))
print(sol.topKFrequent([3,0,1,0], 1))
print(sol.topKFrequent([5,2,5,3,5,3,1,1,3], 2))