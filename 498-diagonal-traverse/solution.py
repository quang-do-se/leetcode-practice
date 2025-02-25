from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up_right_direction = (-1, 1)
        down_left_direction = (1,- 1)

        height = len(mat)
        width = len(mat[0])

        res = []

        direction = up_right_direction
        cell = (0, 0)

        while True:
            res.append(mat[cell[0]][cell[1]])

            if cell[0] == height - 1 and cell[1] == width - 1:
                return res
            
            next_row = cell[0] + direction[0]
            next_col = cell[1] + direction[1]
            
            switch_direction = False

            if next_row < 0 or next_row > height - 1:
                next_row = cell[0]
                next_col = cell[1] + 1
                switch_direction = True

            if next_col < 0 or next_col > width - 1:
                next_row = cell[0] + 1
                next_col = cell[1]
                switch_direction = True
            
            if switch_direction:
                if direction == up_right_direction:
                    direction = down_left_direction
                else:
                    direction = up_right_direction

            cell = (next_row, next_col)


sol = Solution()
print(sol.findDiagonalOrder([[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18], [19,20,21,22,23,24], [25,26,27,28,29,30], [31,32,33,34,35,36]]))
print(sol.findDiagonalOrder([[1,2,3], [4,5,6], [7,8,9]]))
print(sol.findDiagonalOrder([[1,2], [3,4]]))