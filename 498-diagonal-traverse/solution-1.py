from typing import List


class Solution:
    # One of the fastest solution on LeetCode, it processes diagonals in pair
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1:
            return mat[0]

        array = []
        height, width = len(mat), len(mat[0])
        row, col = 0, 0

        while row < height and col < width:
            while row >= 0 and col < width:
                print(f"Add {row,col}")
                array.append(mat[row][col])
                row -= 1
                col += 1
            row += 1
            if col == width:
                row += 1
                col -= 1

            print(row, col)
            print("Process the neighbor diagonal in reverse order")

            while row < height and col >= 0:
                print(f"Add {row,col}")
                array.append(mat[row][col])
                col -= 1
                row += 1
            col += 1
            if row == height:
                row -= 1
                col += 1
            print(row, col)

            print(f"Finish one loop: {array}")
            print()

        return array


sol = Solution()
print(sol.findDiagonalOrder([[1,2,3], [4,5,6], [7,8,9]]))