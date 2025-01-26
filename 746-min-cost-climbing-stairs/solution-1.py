from typing import List


class Solution:
    # Memoization approach
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memoi = {}
        return min(self.min_cost_climbing_stairs(0, cost), self.min_cost_climbing_stairs(1, cost))

    def min_cost_climbing_stairs(self, index: int, cost: List[int]) -> int:
        if index in self.memoi:
            return self.memoi[index]
        if index >= len(cost) - 2:
            return cost[index]
        
        self.memoi[index] = cost[index] + min(self.min_cost_climbing_stairs(index + 1, cost), self.min_cost_climbing_stairs(index + 2, cost))
        return self.memoi[index]


sol = Solution()
""" print(sol.minCostClimbingStairs([1,2]))
print(sol.minCostClimbingStairs([1,1,2]))
print(sol.minCostClimbingStairs([1]))
print(sol.minCostClimbingStairs([2])) """
""" print(sol.minCostClimbingStairs([1,1,100,1])) """
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(sol.minCostClimbingStairs([10,15,20]))