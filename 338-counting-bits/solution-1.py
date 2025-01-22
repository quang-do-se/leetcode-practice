from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Dynamic Programming approach
        #
        # Transition function:
        # P(x + b) = P(x) + 1 where b is 2^m and b > x
        #
        # Examples:
        # P(0)  = 0                                      # base case
        # 
        # P(1)  = P(0 + 1) = P(0 + 2^0) = P(0) + 1 = 1
        # 
        # P(2)  = P(0 + 2) = P(0 + 2^1) = P(0) + 1 = 1
        # P(3)  = P(1 + 2) = P(1 + 2^1) = P(1) + 1 = 2
        # 
        # P(4)  = P(0 + 4) = P(0 + 2^2) = P(0) + 1 = 1
        # P(5)  = P(1 + 4) = P(1 + 2^2) = P(1) + 1 = 2
        # P(6)  = P(2 + 4) = P(2 + 2^2) = P(2) + 1 = 2
        # P(7)  = P(3 + 4) = P(3 + 2^2) = P(3) + 1 = 3
        #
        # P(8)  = P(0 + 8) = P(0 + 2^3) = P(0) + 1 = 1
        # P(9)  = P(1 + 8) = P(1 + 2^3) = P(1) + 1 = 2
        # P(10) = P(2 + 8) = P(2 + 2^3) = P(2) + 1 = 2
        # P(11) = P(3 + 8) = P(3 + 2^3) = P(3) + 1 = 3
        # P(12) = P(4 + 8) = P(4 + 2^3) = P(4) + 1 = 2
        # P(13) = P(5 + 8) = P(5 + 2^3) = P(5) + 1 = 3
        # P(14) = P(6 + 8) = P(6 + 2^3) = P(6) + 1 = 3
        # P(15) = P(7 + 8) = P(7 + 2^3) = P(7) + 1 = 4

        res = [0] * (n + 1)
        x = 0
        b = 1

        while b <= n:   # same as x + b <= n but x is always 0
            while x < b and x + b <= n:
                res[x + b] = res[x] + 1
                x += 1
            x = 0
            b <<= 1

        return res

sol = Solution()


print(sol.countBits(2) == [0,1,1])
print(sol.countBits(5) == [0,1,1,2,1,2])
print(sol.countBits(7) == [0, 1, 1, 2, 1, 2, 2, 3])
print(sol.countBits(15) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4])