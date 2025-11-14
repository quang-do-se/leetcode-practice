from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0

        up_min = prices[0]
        up_profit = 0

        for price in prices:
            # if there is a down turn, take profit
            if price - up_min < up_profit:
                if up_profit > 0:
                    total_profit += up_profit
                # capture the start of new up turn
                up_min = price
                up_profit = 0
            # get new profit if the up turn continues
            else:
                up_profit = price - up_min

        if up_profit > 0:
            total_profit += up_profit

        return total_profit
                
                    



sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([1,2,3,4,5]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([7,1,3,3,6,2,5,3,8]))