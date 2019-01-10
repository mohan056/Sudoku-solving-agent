import math


class SudokuBoard:
    def __init__(self):
        self.board = []
        for i in range(9):
            self.board.append([0] * 9)
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
        for row in self.board:
            if 0 in row:
                return False
        return True

    def is_valid_full(self):
        for i in range(9):
            for j in range(9):
                elem = self.element(i, j)
                if self.row_duplicates_exist(elem, i):
                    return False
                if self.column_duplicates_exist(elem, j):
                    return False
                if self.box_duplicates_exist(elem, i//3, j//3):
                    return False
        return True

    def build_board(self):
        col_counter = 0
        for row_counter in range(9):
            row = input(f"Enter Row {row_counter+1}: ")
            values = row.split(' ')
            if len(values) == 9:
                for value in values:
                    self.add_element(row_counter, col_counter, int(value))
                    col_counter += 1
            elif len(values) == 10:
                for value in values[:-1]:
                    self.add_element(row_counter, col_counter, int(value))
                    col_counter += 1
            else:
                print("Invalid input. Please try again")
            col_counter = 0
            print(len(values))
            print(values)
            print(row)






