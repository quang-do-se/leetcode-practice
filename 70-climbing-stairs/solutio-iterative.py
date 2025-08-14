class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 1
        res[1] = 1

        for i in range(2, n + 1):
            res[i] = res[i - 1] + res[i - 2]

        return res[n]


sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(4))