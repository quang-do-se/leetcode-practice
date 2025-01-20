from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        original_highest_candies = max(candies)

        new_list = []

        for candie in candies:
            new_list.append(candie + extraCandies >= original_highest_candies)

        return new_list


sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3) == [True,True,True,False,True] )
print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1) == [True, False, False, False, False])
print(sol.kidsWithCandies([12, 1, 12], 10) == [True, False, True])
