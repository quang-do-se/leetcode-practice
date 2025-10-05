from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min = float("inf")
        max = float("-inf")
        for n in nums:
            if n < min:
                min = n
            if n > max:
                max = n

        count_arr = [0] * (max - min + 1)
        
        for n in nums:
            count_arr[n - min] += 1

        for i in range(len(count_arr) - 1, -1, -1):
            k -= count_arr[i]

            if k <= 0:
                return i + min
            
        return -1
        


sol = Solution()
print(sol.findKthLargest([-3,2,1,6,6,4], 2))
print(sol.findKthLargest([3,2,1,5,6,4], 2) == 5)