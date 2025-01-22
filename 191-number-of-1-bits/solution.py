class Solution:
    def hammingWeight(self, n: int) -> int:
        val = 0
        while n != 0:
            val += n & 1
            n = n >> 1
        return val
    

sol = Solution()
print(sol.hammingWeight(11) == 3)
print(sol.hammingWeight(128) == 1)
print(sol.hammingWeight(2147483645) == 30)