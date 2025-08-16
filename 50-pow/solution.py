class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        if n < 0:
            x = 1 / x
            n = -n

        while n > 0:
            if n % 2 == 1:
                res *= x

            x *= x

            n //= 2
        return res


sol = Solution()

print(sol.myPow(2, 5) == 32)
print(sol.myPow(2.0, -2) == 0.25)
print(sol.myPow(2.0, -3) == 0.125)
print(sol.myPow(2.0, 0) == 1)
print(sol.myPow(2.0, 1) == 2)
print(sol.myPow(2.0, -1) == 0.5)

