from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n - 1

        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m

        k = h

        l = 0
        h = n - 1

        while l <= h:
            m = (l + h) // 2
            m_with_offset = (m + k) % n
            m_val = nums[m_with_offset]

            if m_val == target:
                return m_with_offset
            elif target < m_val:
                h = m - 1
            else:
                l = m + 1

        return -1


sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))
print(sol.search([4,5,6,7,0,1,2], 3))
print(sol.search([4,5,6,7,0,1,2], 1))