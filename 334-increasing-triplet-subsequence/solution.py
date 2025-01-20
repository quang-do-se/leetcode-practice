from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = second_smallest = float("inf")

        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second_smallest:
                second_smallest = n
            else:
                return True

        return False


sol = Solution()
print(sol.increasingTriplet([4,5,2147483647,1,2]) == True)
print(sol.increasingTriplet([1,2,3,4,5]) == True)
print(sol.increasingTriplet([5,4,3,2,1]) == False)
print(sol.increasingTriplet([2,1,5,0,4,6]) == True)
print(sol.increasingTriplet([1]) == False)
print(sol.increasingTriplet([1,1]) == False)
print(sol.increasingTriplet([1,1,1]) == False)
print(sol.increasingTriplet([1,2,2]) == False)
print(sol.increasingTriplet([1,2,3]) == True)
print(sol.increasingTriplet([1,5,0,10,5,7,3]) == True)
print(sol.increasingTriplet([10,5,12,7,1,9]) == True)