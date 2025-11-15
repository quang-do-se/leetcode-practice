from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        valley = peak = prices[0]

        for price in prices:
            if price < peak:
                # Take profit
                total_profit += peak - valley
                valley = peak = price
            else:
                # Capture new peak
                peak = price

        total_profit += peak - valley

        return total_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]) == 7)
print(sol.maxProfit([1, 2, 3, 4, 5]) == 4)
print(sol.maxProfit([7, 6, 4, 3, 1]) == 0)
print(sol.maxProfit([7, 1, 3, 3, 6, 2, 5, 3, 8]) == 13)
