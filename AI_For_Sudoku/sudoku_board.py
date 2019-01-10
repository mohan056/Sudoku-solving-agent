import math


class SudokuBoard:
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append([-1] * 9)
        self.filled = False

    def add_element(self, i, j, value):
        if i > 8 or j > 8 or i < 0 or j < 0:
            print("This is not possible")
        else:
            self.board[i][j] = value

    def element(self, i, j):
        return self.board[i][j]

    def row_duplicates_exist(self, value, i):
        row = self.board[i]
        return row.count(value) > 1

    def column_duplicates_exist(self, value, j):
        column = [
            self.element(0, j),
            self.element(1, j),
            self.element(2, j),
            self.element(3, j),
            self.element(4, j),
            self.element(5, j),
            self.element(6, j),
            self.element(7, j),
            self.element(8, j)
        ]
        return column.count(value) > 1

    def box_duplicates_exist(self, value, i, j):
        sri = i * 3
        sci = j * 3
        box = [
            self.element(sri, sci), self.element(sri+1, sci), self.element(sri+2, sci),
            self.element(sri, sci+1), self.element(sri+1, sci+1), self.element(sri+2, sci+1),
            self.element(sri, sci+2), self.element(sri+1, sci+2), self.element(sri+2, sci+2)
        ]
        return box.count(value) > 1

    def __str__(self):
        board_str = ''
        for i in range(9):
            for j in range(9):
                if j % 3 == 0:
                    board_str = board_str + '|'
                board_str = board_str + str(self.element(i, j))
            board_str = board_str + '\n'
            if (i+1)%3 == 0:
                board_str = board_str + '-------------'
                board_str = board_str + '\n'
        return board_str

    def is_full(self):
        count = 0
        for row in self.board:
            if -1 in row:
                return False
        return True






