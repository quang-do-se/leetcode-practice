from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        for e in nums1:
            dict1[e] = dict1.get(e, 0) + 1

        res = []
        for e in nums2:
            if e in dict1 and dict1[e] > 0:
                res.append(e)
                dict1[e] -= 1

        return res


sol = Solution()
print(sol.intersect([1,2,2,1], [2,2]))
print(sol.intersect([4,9,5], [9,4,9,8,4]))