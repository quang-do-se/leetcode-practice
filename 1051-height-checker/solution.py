from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freq = [0] * 101
        for val in heights:
            freq[val] = freq[val] + 1

        # prefix sum of frequencies
        for i in range(2, len(freq)):
            freq[i] += freq[i - 1]

        not_in_order_count = 0
        for i in range(0, len(heights)):
            val = heights[i]
            if i < freq[val - 1] or i >= freq[val]:
                not_in_order_count += 1

        return not_in_order_count


sol = Solution()
print(sol.heightChecker([1,1,4,2,1,3]) == 3)
print(sol.heightChecker([5,1,2,3,4]) == 5)
print(sol.heightChecker([1,2,3,4,5]) == 0)