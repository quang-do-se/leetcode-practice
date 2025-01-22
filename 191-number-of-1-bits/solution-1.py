class Solution:
    def hammingWeight(self, n: int) -> int:
        val = 0
        while n != 0:
            n = n & (n - 1)  # flip the least-significant 1-bit in `n`` to 0
            val += 1
        return val
    

sol = Solution()
print(sol.hammingWeight(11) == 3)
print(sol.hammingWeight(128) == 1)
print(sol.hammingWeight(2147483645) == 30)