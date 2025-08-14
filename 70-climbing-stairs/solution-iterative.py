class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        res = [0] * (n + 1)
        res[1] = 1
        res[2] = 2

        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2]

        return res[n]


sol = Solution()
print(sol.climbStairs(1) == 1)
print(sol.climbStairs(2) == 2)
print(sol.climbStairs(3) == 3)
print(sol.climbStairs(4) == 5)