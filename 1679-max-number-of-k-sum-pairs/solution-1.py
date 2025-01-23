from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        map = {}

        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1

        res = 0
        for n in map:
            if map[n] == -1:
                continue

            search = k - n
            if search in map:
                if n == search:
                    res += map[search] // 2
                else:
                    res += min(map[n], map[search])

                map[search] = -1
                
        return res


sol = Solution()
print(sol.maxOperations([1,2,3,4], 5))
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