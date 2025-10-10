from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)
        freq = [0] * (max_weight + 1)

        for stone in stones:
            freq[stone] += 1

        i = max_weight

        while i > 0:
            if freq[i] == 0:
                i -= 1
            else:
                freq[i] -= 1
                j = i
                while j > 0 and freq[j] == 0:
                    j -= 1

                if j > 0:
                    freq[j] -= 1
                    freq[i - j] += 1
                else:
                    return i
        
        return 0
                


sol = Solution()
print(sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1)
print(sol.lastStoneWeight([1]) == 1)
print(sol.lastStoneWeight([1, 4]) == 3)
print(sol.lastStoneWeight([2, 2]) == 0)
print(sol.lastStoneWeight([2]))
