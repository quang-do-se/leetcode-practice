from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        height = len(matrix)
        width = len(matrix[0])
        
        row = col = 0
        visited = {}
        res = []

        current_direction = [0, 1]
        for _ in range(height * width):
            res.append(matrix[row][col])
            visited[(row,col)] = None

            new_row = row + current_direction[0]
            new_col = col + current_direction[1]

            if new_row < 0 or new_row > height - 1 or new_col < 0 or new_col > width - 1 or (new_row, new_col) in visited:
                current_direction[0], current_direction[1] = current_direction[1], current_direction[0] * -1
                new_row = row + current_direction[0]
                new_col = col + current_direction[1]
            
            row, col = new_row, new_col

        return res


sol = Solution()    
print(sol.spiralOrder([[1]]) == [1])
print(sol.spiralOrder([[1,2,3], [4,5,6], [7,8,9]]) == [1,2,3,6,9,8,7,4,5])
print(sol.spiralOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7])