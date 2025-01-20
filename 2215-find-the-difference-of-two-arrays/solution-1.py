from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Python built-in solution
        diff1 = set(nums1).difference(set(nums2))
        diff2 = set(nums2).difference(set(nums1))

        return[list(diff1) , list(diff2)]


sol = Solution()
print(sol.findDifference([1,2,3] ,[2,4,6]) == [[1,3],[4,6]])
print(sol.findDifference([1,2,3,3] ,[1,1,2,2]) == [[3],[]])