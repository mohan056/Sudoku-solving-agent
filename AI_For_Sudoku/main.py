from sudoku_solver import SudokuSolver
from sudoku_board import SudokuBoard


def main():
    board = SudokuBoard()
    board.add_element(0, 3, 3)
    board.add_element(0, 4, 4)
    board.add_element(0, 5, 6)
    board.add_element(0, 7, 5)
    board.add_element(0, 8, 9)

    ###########

    # board.add_element(0, 0, 5)
    # board.add_element(0, 1, 3)
    # board.add_element(0, 4, 7)
    # board.add_element(1, 0, 6)
    # board.add_element(1, 3, 1)
    # board.add_element(1, 4, 9)
    # board.add_element(1, 5, 5)
    # board.add_element(2, 1, 9)
    # board.add_element(2, 2, 8)
    # board.add_element(2, 7, 6)
    # board.add_element(3, 0, 8)
    # board.add_element(3, 4, 6)
    # board.add_element(3, 8, 3)
    # board.add_element(4, 0, 4)
    # board.add_element(4, 3, 8)
    # board.add_element(4, 5, 3)
    # board.add_element(4, 8, 1)
    # board.add_element(5, 0, 7)
    # board.add_element(5, 4, 2)
    # board.add_element(5, 8, 6)
    # board.add_element(6, 1, 6)
    # board.add_element(6, 6, 2)
    # board.add_element(6, 7, 8)
    # board.add_element(7, 3, 4)
    # board.add_element(7, 4, 1)
    # board.add_element(7, 5, 9)
    # board.add_element(7, 8, 5)
    # board.add_element(8, 4, 8)
    # board.add_element(8, 7, 7)
    # board.add_element(8, 8, 9)
    # board.build_board()
    solver = SudokuSolver(board)
    if solver.board.is_valid_full():
        print("Board before solving: \n")
        print(board, "\n")
        if solver.backtracking(0, 0):
            print("Sudoku has been solved \n")
        print(board)
        if solver.board.is_valid_full():
            print("Solution Exists!!")
    else:
        print("Board entered is not valid. Please enter a valid board.")

main()