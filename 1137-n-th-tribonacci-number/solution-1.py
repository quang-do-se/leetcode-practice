class Solution:
    cache = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.cache[n]
    
sol = Solution()
print(sol.tribonacci(0) == 0)
print(sol.tribonacci(1) == 1)
print(sol.tribonacci(2) == 1)
print(sol.tribonacci(4) == 4)
print(sol.tribonacci(25) == 1389537)