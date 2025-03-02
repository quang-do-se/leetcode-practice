from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            last_val = nums[n - 1]
            for j in range(n - 1, 0, - 1):
                nums[j] = nums[j - 1]
            nums[0] = last_val

sol = Solution()
l = [1,2,3,4,5,6,7]
sol.rotate(l, 3)
print(l)

l = [-1,-100,3,99]
sol.rotate(l, 2)
print(l)