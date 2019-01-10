from sudoku_solver import SudokuSolver
from sudoku_board import SudokuBoard


def main():
    board = SudokuBoard()
    board.add_element(0, 0, 5)
    board.add_element(0, 1, 3)
    board.add_element(0, 4, 7)
    board.add_element(1, 0, 6)
    board.add_element(1, 3, 1)
    board.add_element(1, 4, 9)
    board.add_element(1, 5, 5)
    board.add_element(2, 1, 9)
    board.add_element(2, 2, 8)
    board.add_element(2, 1, 9)
    board.add_element(2, 1, 9)
    board.add_element(1, 0, 6)
    solver = SudokuSolver(board)
    print(solver.backtracking(0, 0))
    # flag = solver.check_contraints_apply()
    print(board)

main()