from typing import List
import heapq

#  Bucket Sort solution - O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        frequency = {}
        for n in nums:
            frequency[n] = frequency.get(n, 0) + 1
        
        # Build a bucket list for 0 to n frequency
        bucket = [[] for _ in range(len(nums) + 1)] 

        for n in frequency:
            bucket[frequency.get(n)].append(n)

        res = []
        for i in range(len(nums), -1, -1):
            if bucket[i]:
                res += bucket[i]

            if len(res) >= k:
                return res

        return res


sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([-1, -1], 1))
print(sol.topKFrequent([3,0,1,0], 1))
print(sol.topKFrequent([5,2,5,3,5,3,1,1,3], 2))