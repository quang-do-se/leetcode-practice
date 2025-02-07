from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1            


sol = Solution()

nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2,5,6], 3)
print(nums1)

nums1 = [1]
sol.merge(nums1, 1, [], 0)
print(nums1)

nums1 = [0]
sol.merge(nums1, 0, [1], 1)
print(nums1)
