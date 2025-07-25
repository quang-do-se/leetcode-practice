from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_len = 9
        y_len = 9
        boxes_x_len = 3
        boxes_y_len = 3

        rows = [set() for _ in range(x_len)]
        cols = [set() for _ in range(y_len)]
        boxes = [set() for _ in range(boxes_x_len * boxes_y_len)]

        for row in range(len(board)):
            for col in range(len(board[row])):
                cell_val = board[row][col]
                if cell_val == ".":
                    continue

                if cell_val in rows[row]:
                    #print(f"False with val {cell_val} on row {row}")
                    return False
                rows[row].add(cell_val)

                if cell_val in cols[col]:
                    #print(f"False with val {cell_val} on col {col}")
                    return False
                cols[col].add(cell_val)

                box_index = row // boxes_x_len * boxes_y_len + col // boxes_y_len

                if cell_val in boxes[box_index]:
                    #print(f"False with val {cell_val} in box {box_index}")
                    return False
                boxes[box_index].add(cell_val)

        return True

board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

sol = Solution()
print(sol.isValidSudoku(board1) == True)
print(sol.isValidSudoku(board2) == False)