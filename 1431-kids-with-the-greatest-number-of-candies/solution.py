class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        original_highest_candies = max(candies)

        new_list = []

        for candie in candies:
            new_list.append(candie + extraCandies >= original_highest_candies)

        return new_list

sol = Solution()
print(sol.kidsWithCandies([2, 3, 5, 1, 3], 3))
print(sol.kidsWithCandies([4, 2, 1, 1, 2], 1))
print(sol.kidsWithCandies([12, 1, 12], 10))
