from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        up_right_direction = (-1, 1)
        down_left_direction = (1, -1)

        height = len(mat)
        width = len(mat[0])
        last_row = height - 1
        last_col = width - 1

        res = []

        direction = up_right_direction
        row, col = 0, 0

        while row < height and col < width:
            res.append(mat[row][col])

            next_row = row + direction[0]
            next_col = col + direction[1]

            switch_direction = False

            # Attempt to move to the right of the current cell if we are out of bound
            if next_row < 0 or next_row > last_row:
                next_row = row
                next_col = col + 1
                switch_direction = True

            # If we cannot move to the right, then move down to the next row below the current cell
            if next_col < 0 or next_col > last_col:
                next_row = row + 1
                next_col = col
                switch_direction = True

            if switch_direction:
                if direction == up_right_direction:
                    direction = down_left_direction
                else:
                    direction = up_right_direction

            row, col = next_row, next_col

        return res


sol = Solution()
print(sol.findDiagonalOrder([[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18], [19,20,21,22,23,24], [25,26,27,28,29,30], [31,32,33,34,35,36]]) == [1, 2, 7, 13, 8, 3, 4, 9, 14, 19, 25, 20, 15, 10, 5, 6, 11, 16, 21, 26, 31, 32, 27, 22, 17, 12, 18, 23, 28, 33, 34, 29, 24, 30, 35, 36])
print(sol.findDiagonalOrder([[1,2,3], [4,5,6], [7,8,9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9])
print(sol.findDiagonalOrder([[1,2], [3,4]]) == [1, 2, 3, 4])