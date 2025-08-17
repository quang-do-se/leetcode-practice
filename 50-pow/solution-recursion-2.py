class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        
        if n % 2 == 1:
            return x * self.myPow(x * x, (n - 1) // 2)
        
        return self.myPow(x * x, n // 2)


sol = Solution()

print(sol.myPow(2, 0))
print(sol.myPow(2, 1))
print(sol.myPow(2, 3))
print(sol.myPow(2, 5))
print(sol.myPow(2, -1))
print(sol.myPow(2, -2))
print(sol.myPow(2, -3))

