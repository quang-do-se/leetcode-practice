class Solution:
    cache = {0: 0, 1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]


sol = Solution()
print(sol.climbStairs(1) == 1)
print(sol.climbStairs(2) == 2)
print(sol.climbStairs(3) == 3)
print(sol.climbStairs(4) == 5)
