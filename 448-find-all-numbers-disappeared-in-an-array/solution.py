from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq = [0] * (len(nums) + 1)

        for e in nums:
            freq[e] += 1

        res = []
        for i in range(1, len(freq)):
            if freq[i] == 0:
                res.append(i)

        return res


sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5, 6])
print(sol.findDisappearedNumbers([1, 1]) == [2])
print(sol.findDisappearedNumbers([1]) == [])