import math
from sudoku_board import SudokuBoard

class SudokuSolver:
    def __init__(self, board: SudokuBoard):
        self.board = board
        self.found = False

    def check_contraints_apply(self, value, row, column):
        rows_flag = True
        columns_flag = True
        box_flag = True
        rows_flag = rows_flag and self.board.row_duplicates_exist(value, row)
        columns_flag = columns_flag and self.board.column_duplicates_exist(value, column)

        box_flag = box_flag and self.board.box_duplicates_exist(value, row//3, column//3)
        return not(rows_flag or columns_flag or box_flag)

    def backtracking(self, i, j):
        print(i, ", ", j)
        if self.board.is_full():
            return True
        else:
            if self.board.element(i, j) == 0:
                for val in range(1, 10):
                    self.board.add_element(i, j, val)
                    if self.check_contraints_apply(val, i, j):
                        flag = False
                        if i == 8 and j < 8:
                            flag = self.backtracking(0, j+1)
                        elif i < 8 and j <= 8:
                            flag = self.backtracking(i+1, j)
                        elif i == 8 and j == 8:
                            return True
                        if flag:
                            return flag
                self.board.add_element(i, j, 0)
                return False
            else:
                if i == 8 and j < 8:
                    return self.backtracking(0, j + 1)
                elif i < 8 and j <= 8:
                    return self.backtracking(i + 1, j)
                elif i == 8 and j == 8:
                    return True



