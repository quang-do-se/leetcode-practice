from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        total = height * width

        col_len = width
        row_len = height - 1

        direction = 1
        row = col = 0
        res = []

        while len(res) < total:
            for _ in range(col_len): 
                res.append(matrix[row][col])
                col += direction
            col -= direction
            
            row += direction   # Skip overlapping cell between horizontal traverse and vertical traverse

            for _ in range(row_len):
                res.append(matrix[row][col])
                row += direction
            row -= direction

            direction *= -1   # Change direction
            col += direction

            col_len -= 1
            row_len -= 1

        return res


sol = Solution()    
print(sol.spiralOrder([[1]]) == [1])
print(sol.spiralOrder([[1,2,3], [4,5,6], [7,8,9]]) == [1,2,3,6,9,8,7,4,5])
print(sol.spiralOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7])
print(sol.spiralOrder([[7], [9], [6]]) == [7, 9, 6])