from typing import List


class Solution:
    # Brute force approach
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.min_cost_climbing_stairs(0, cost), self.min_cost_climbing_stairs(1, cost))

    def min_cost_climbing_stairs(self, index: int, cost: List[int]) -> int:
        if index >= len(cost) - 2:
            return cost[index]

        total_cost = cost[index] + min(self.min_cost_climbing_stairs(index + 1, cost), self.min_cost_climbing_stairs(index + 2, cost))
        return total_cost


sol = Solution()
print(sol.minCostClimbingStairs([1,2]) == 1)
print(sol.minCostClimbingStairs([1,1,2]) == 1)
print(sol.minCostClimbingStairs([1,1,100,1]) == 2)
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6)
print(sol.minCostClimbingStairs([10,15,20]) == 15)