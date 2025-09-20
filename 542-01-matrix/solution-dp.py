from math import inf
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dp = [row[:] for row in mat]
        m, n = len(dp), len(dp[0])

        for row in range(m):
            for col in range(n):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row > 0:
                        min_neighbor = min(min_neighbor, dp[row - 1][col])
                    if col > 0:
                        min_neighbor = min(min_neighbor, dp[row][col - 1])
                        
                    dp[row][col] = min_neighbor + 1
    
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                min_neighbor = inf
                if dp[row][col] != 0:
                    if row < m - 1:
                        min_neighbor = min(min_neighbor, dp[row + 1][col])
                    if col < n - 1:
                        min_neighbor = min(min_neighbor, dp[row][col + 1])
                        
                    dp[row][col] = min(dp[row][col], min_neighbor + 1)

        return dp
    

sol = Solution()
print(
    sol.updateMatrix([[0, 1, 1], [1, 1, 1], [1, 1, 0]])
    == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
)    