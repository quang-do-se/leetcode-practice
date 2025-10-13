from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        row_col_pointers = [0] * n

        for i in range(k):
            min_row_value = float("inf")
            min_row_index = -1

            for r in range(n):
                if row_col_pointers[r] >= n:
                    continue

                val = matrix[r][row_col_pointers[r]]
                if val < min_row_value:
                    min_row_value = val
                    min_row_index = r

            row_col_pointers[min_row_index] += 1

        return min_row_value


sol = Solution()

print(sol.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
print(sol.kthSmallest([[1, 3, 10], [1, 4, 10], [1, 5, 10]], 8))
print(sol.kthSmallest([[-5]], 1))
