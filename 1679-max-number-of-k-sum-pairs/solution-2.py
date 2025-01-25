from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        map = {}
        res = 0
        for n in nums:
            search = k - n

            if search in map and map[search] > 0:
                res += 1
                map[search] -= 1
            else:
                if n in map:
                    map[n] += 1
                else:
                    map[n] = 1
        
        return res


sol = Solution()
print(sol.maxOperations([3,1,3,4,3], 6))

print(sol.maxOperations([1,2,3,4], 5) == 2)
print(sol.maxOperations([3,1,3,4,3], 6) == 1)
print(sol.maxOperations([3], 3) == 0)
print(sol.maxOperations([3,0], 3) == 1)
print(sol.maxOperations([0,3], 3) == 1)
print(sol.maxOperations([3,3], 6) == 1)
print(sol.maxOperations([5,5,5,5], 10) == 2)
print(sol.maxOperations([5,5,5,5], 5) == 0)
print(sol.maxOperations([5,5,5], 10) == 1)
print(sol.maxOperations([5,5], 10) == 1)
print(sol.maxOperations([5], 10) == 0)
print(sol.maxOperations([5], 5) == 0)
print(sol.maxOperations([5], 0) == 0)
print(sol.maxOperations([2,1,1,1,2,1,2,2,2,2], 3) == 4)
print(sol.maxOperations([2,1,1,1,2,1,2,1,2,2,2,2], 3) == 5)