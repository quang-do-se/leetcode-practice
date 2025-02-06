from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Two passes
        new_len = 0
        last_index = 0
        zero_count = 0

        # Get the last index in the old array
        while last_index < len(arr):
            if arr[last_index] == 0:
                zero_count += 1
                new_len += 1
            new_len += 1

            if new_len >= len(arr):
                break
            last_index += 1

        new_index = len(arr) - 1

        # Copy array in-place. If we move item to the right, it's safer to start from the end of the array in reverse direction
        while new_index >= 0:
            if arr[last_index] == 0:
                arr[new_index] = 0

                # Don't duplicate the last 0
                if last_index + zero_count - 1 < len(arr) - 1:
                    new_index -= 1
                    arr[new_index] = 0
                zero_count -= 1
            else:
                arr[new_index] = arr[last_index]

            new_index -= 1
            last_index -= 1



sol = Solution()

arr = [1,0,2,3,0,4,5,0]
sol.duplicateZeros(arr)
print(arr == [1, 0, 0, 2, 3, 0, 0, 4])


arr = [0,2,0,0,5,0]
sol.duplicateZeros(arr)
print(arr == [0, 0, 2, 0, 0, 0])


arr = [0,0,0]
sol.duplicateZeros(arr)
print(arr == [0, 0, 0])

arr = [0,0,1,0,0]
sol.duplicateZeros(arr)
print(arr == [0, 0, 0, 0, 1])

arr = [1,2,3]
sol.duplicateZeros(arr)
print(arr == [1, 2, 3])

arr = [0]
sol.duplicateZeros(arr)
print(arr == [0])


arr = [1,5,2,0,6,8,0,6,0]
sol.duplicateZeros(arr)
print(arr)
print(arr == [1,5,2,0,0,6,8,0,0])