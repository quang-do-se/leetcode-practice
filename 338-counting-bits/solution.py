from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            val = 0
            while i != 0:
                i = i & (i - 1)
                val += 1
            res.append(val)

        return res

sol = Solution()


print(sol.countBits(2) == [0,1,1])
print(sol.countBits(5) == [0,1,1,2,1,2])