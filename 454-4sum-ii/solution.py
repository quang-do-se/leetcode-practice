from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum1 = {}
        sum2 = {}
        res = 0

        for n1 in nums1:
            for n2 in nums2:
                sum1[n1 + n2] = sum1.get(n1 + n2, 0) + 1

        for n3 in nums3:
            for n4 in nums4:
                sum2[n3 + n4] = sum2.get(n3 + n4, 0) + 1

        for s1 in sum1:
            complement = 0 - s1
            if complement in sum2:
                res += sum1[s1] * sum2[complement]

        return res


sol = Solution()
print(sol.fourSumCount([-1,-1], [-1, 1], [-1, 1], [1, -1]) == 6)
print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2)
print(sol.fourSumCount([0], [0], [0], [0]) == 1)
