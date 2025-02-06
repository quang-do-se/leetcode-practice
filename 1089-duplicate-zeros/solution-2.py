from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Most elegant solution: https://leetcode.com/problems/duplicate-zeros/solutions/322576/python-3-real-in-place-solution/

        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            # Write original number in the new position, if the position can fit in the original array
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]

            # Write the duplicate zero
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0



"""
# Algorithm Explanation

Let's say we have this array:
[0,2,0,0,5,0]

It has 4 zeros in the original array.
Each zero causes a shift to the right for subsequent elements.
The new expanded array will be (O means a duplicate 0):

org: [0,2,0,0,5,0]
new: [O,0,2,O,0,O,0,5,O,0]

The position of each element in the new array will be
new_index = original_index + number_of_zeros_before_it_in_the_original_array

For example, to get the new index of the last element, in this case 5, we have:
next_index = 5 + 4 = 9

# Algorithm Execution

Start with the last index in original array to prevents overwriting original values

number_of_zero = 4
org[5] = 0:
    The new position is 5 + 4 = 9
    Does index 9 fit in the original array? No, do nothing
    Is it a zero? Yes, since it's a zero, we know the padding zero is just before this original zero
    We can get the padding zero index by 5 + (4 - 1) = 8 and we can reduce the number of zero to 3 in the same step
    Does the padding zero index 8 fit in the original array? No, do nothing
Result: [0,2,0,0,5,0]

number_of_zero = 3
org[4] = 5
    The new position is 4 + 3 = 7
    Does index 7 fit in the origib.nal array? No, do nothing
    Is it a zero? No, do nothing
Result: [0,2,0,0,5,0]

number_of_zero = 3
org[3] = 0:
    The new position is 3 + 3 = 6
    Does index 6 fit in the original array? No, do nothing
    Is it a zero? Yes, since it's a zero, we know the padding zero is just before this original zero
    We can get the padding zero index by 3 + (3 - 1) = 5 and we can reduce the number of zero to 2 in the same step
    Does the padding zero index 5 fit in the original array? Yes, write it to index 5
Result: [0,2,0,0,5,0]

number_of_zero = 2
org[2] = 0:
    The new position is 2 + 2 = 4
    Does index 4 fit in the original array? Yes, write it to index 4
Result: [0,2,0,0,0,0]
    Is it a zero? Yes, since it's a zero, we know the padding zero is just before this original zero
    We can get the padding zero index by 2 + (2 - 1) = 3 and we can reduce the number of zero to 1 in the same step
    Does the padding zero index 3 fit in the original array? Yes, write it to index 3
Result: [0,2,0,0,0,0]

number_of_zero = 1
org[1] = 2:
    The new position is 2 + 1 = 3
    Does index 3 fit in the original array? Yes, write it to index 3
    Is it a zero? No, do nothing
Result: [0,2,2,0,0,0]

number_of_zero = 1
org[0] = 0:
    The new position is 0 + 1 = 1
    Does index 1 fit in the original array? Yes, write it to index 1
Result: [0,0,2,0,0,0]
    Is it a zero? Yes, since it's a zero, we know the padding zero is just before this original zero
    We can get the padding zero index by 0 + (1 - 1) = 0 and we can reduce the number of zero to 0 in the same step
    Does the padding zero index 0 fit in the original array? Yes, write it to index 0
Result: [0,0,2,0,0,0]
"""

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
print(arr == [1,5,2,0,0,6,8,0,0])

arr = [1,2,0,3]
sol.duplicateZeros(arr)
print(arr == [1,2,0,0])

arr = [1,2,0]
sol.duplicateZeros(arr)
print(arr == [1,2,0])