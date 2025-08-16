class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        if n == 1:
            return x
        
        res = 1
        if n % 2 == 1:
            res = x
        
        sub_res = self.myPow(x, n // 2)
        return res * sub_res * sub_res


sol = Solution()

print(sol.myPow(2, 0))
print(sol.myPow(2, 1))
print(sol.myPow(2, 3))
print(sol.myPow(2, 5))
print(sol.myPow(2, -1))
print(sol.myPow(2, -2))
print(sol.myPow(2, -3))

