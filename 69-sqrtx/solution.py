class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

sol = Solution()
print(sol.mySqrt(0) == 0)
print(sol.mySqrt(1) == 1)
print(sol.mySqrt(2) == 1)
print(sol.mySqrt(3) == 1)
print(sol.mySqrt(4) == 2)
print(sol.mySqrt(5) == 2)
print(sol.mySqrt(6) == 2)
print(sol.mySqrt(8) == 2)
print(sol.mySqrt(35) == 5)
print(sol.mySqrt(36) == 6)
print(sol.mySqrt(37) == 6)
