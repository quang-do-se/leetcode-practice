from typing import List


class Solution:
    # Memoization approach
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        size = len(cost)
        self.dp = [0] * size
        self.dp[size - 1] = cost[size - 1]
        self.dp[size - 2] = cost[size - 2]

        for i in range(size - 3, -1, -1):
            self.dp[i] = cost[i] + min(self.dp[i + 1], self.dp[i + 2])

        return min(self.dp[0], self.dp[1])
    
sol = Solution()
""" print(sol.minCostClimbingStairs([1,2]))
print(sol.minCostClimbingStairs([1,1,2]))
print(sol.minCostClimbingStairs([1]))
print(sol.minCostClimbingStairs([2])) """
""" print(sol.minCostClimbingStairs([1,1,100,1])) """
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
print(sol.minCostClimbingStairs([10,15,20]))