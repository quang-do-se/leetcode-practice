from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        res = [0] * n

        for i in range(n):
            res[(i + k) % n] = nums[i]
        
        for i in range(n):
            nums[i] = res[i]
        

sol = Solution()
l = [1,2,3,4,5,6,7]
sol.rotate(l, 3)
print(l)

l = [-1,-100,3,99]
sol.rotate(l, 2)
print(l)