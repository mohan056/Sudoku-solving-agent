from sudoku_solver import SudokuSolver
from sudoku_board import SudokuBoard


def main():
    board = SudokuBoard()
    for i in range(1,10):
        board.add_element(0, i, i)
    solver = SudokuSolver(board)
    print(solver.backtracking(0, 0))
    # flag = solver.check_contraints_apply()
    print(board)

main()