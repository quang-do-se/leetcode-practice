from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r1 = m - 1
        r2 = n - 1
        w = m + n - 1

        while r1 >= 0 and r2 >= 0:
            if nums2[r2] > nums1[r1]:
                nums1[w] = nums2[r2]
                r2 -= 1
            else:
                nums1[w] = nums1[r1]
                r1 -= 1
            w -= 1

        while r1 >= 0:
            nums1[w] = nums1[r1]
            w -= 1
            r1 -= 1

        while r2 >= 0:
            nums1[w] = nums2[r2]
            w -= 1
            r2 -= 1


sol = Solution()

nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2,5,6], 3)
print(nums1 == [1, 2, 2, 3, 5, 6])

nums1 = [1]
sol.merge(nums1, 1, [], 0)
print(nums1 == [1])

nums1 = [0]
sol.merge(nums1, 0, [1], 1)
print(nums1 == [1])
