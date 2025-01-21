class Solution:
    cache = {}

    def tribonacci(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n <= 2:
            return 1
        elif n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.cache[n]
    
sol = Solution()
print(sol.tribonacci(0) == 0)
print(sol.tribonacci(1) == 1)
print(sol.tribonacci(2) == 1)
print(sol.tribonacci(4) == 4)
print(sol.tribonacci(25) == 1389537)