from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        cycle_index = 0
        next_index = 0
        next_val = nums[0]

        for _ in range(n):
            swap_index = (next_index + k) % n
            swap_val = next_val

            # Store the swapped value
            next_index = swap_index
            next_val = nums[swap_index]

            # Swapping value
            nums[swap_index] = swap_val

            if next_index == cycle_index and cycle_index < k:
                next_index += 1
                cycle_index += 1
                next_val = nums[next_index]
        

sol = Solution()
l = [1,2,3,4,5,6,7]
sol.rotate(l, 3)
print(l)

l = [-1,-100,3,99]
sol.rotate(l, 2)
print(l)


l = [1]
sol.rotate(l, 0)
print(l)