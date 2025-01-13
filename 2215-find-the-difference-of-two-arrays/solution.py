class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        dict1, dict2 = {}, {}

        for n in set(nums1):
            dict1[n] = None

        for n in set(nums2):
            dict2[n] = None

        diff1, diff2 = [], []
        for key in dict1:
            if key not in dict2:
                diff1.append(key)

        for key in dict2:
            if key not in dict1:
                diff2.append(key)

        return [diff1, diff2]


sol = Solution()
print(sol.findDifference([1,2,3] ,[2,4,6]) == [[1,3],[4,6]])
print(sol.findDifference([1,2,3,3] ,[1,1,2,2]) == [[3],[]])