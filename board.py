from sudoku_generator import *
from cell import Cell
import pygame

generate_sudoku(9, 0)

#API from sudoku_generator and cell to sudoku.py

#Add difficulty buttons
"""
81 cell --> board

sudoku_generator --> board

board --> sudoku
"""

"""
Front End
"""


class Board:
    def __init__(self, width, height, screen, difficulty):
        #Width of Board
        self.width = width
        #Height of Board
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.sudoku_board = generate_sudoku(9, difficulty)
        self.original_board = [[0 for j in range(9)]
                      for i in range(9)]
        self.sudoku_backend = [[0 for i in range(9)]
                      for j in range(9)]


    def print_board(self):
        for i in range(9):
            print(self.original_board[i])
        print("-----------")
        for i in range(9):
            print(self.sudoku_board[i])
        print("-----------")
    def set_sudoku_backend(self):
        self.sudoku_backend = [[Cell(self.sudoku_board[i][j], j * 80, i * 80, self.screen) for i in range(9)]
                               for j in range(9)]

    def set_original_sudoku(self):
        self.original_board = [[self.sudoku_board[i][j] for j in range(9)]
                               for i in range(9)]

    def draw(self):
        for i in range(9):
            for j in range(9):
                Cell.draw(self.sudoku_backend[i][j], False)

        self.draw_border()

    def select(self, row, col):
        #Allows user to select the cell
        row -= 1
        col -= 1
        #Dont know why it is backwards??
        #Will fix eventually
        if self.original_board[col][row] == 0:
            Cell.draw(self.sudoku_backend[row][col], True)

    def click(self, x, y):
        return (x // 80, y // 80)

    def clear(self, x, y):
        #Clears board to regular values
        #If key del is entered, clear that cell
        """
        Switched x and y for self.sudoku_board
        Dont know why
        """

        self.sudoku_board[y][x] = 0
        Cell.set_sketched_value(self.sudoku_backend[x][y], 0)
        Cell.set_cell_value(self.sudoku_backend[x][y], 0)

    def sketch(self, value, x, y):
        #Add function that draws the number if number is input
        font = pygame.font.SysFont("Times New Roman", 25, True, False)
        string_copy = str(value)
        value = font.render(string_copy, False, (128, 128, 128))
        self.screen.blit(value, (x * 80 + 5, y * 80))

    def place_number(self, value, x, y):
        #Sets value of cell to user input
        #Called when user pressses enter key
        font = pygame.font.SysFont("Times New Roman", 50, True, False)
        value = font.render(str(value), False, (0, 0, 0))
        self.screen.blit(value, (x + 107, y + 90))


    def reset_to_original(self):
        """
        Only Works once for some reason
        :return:
        """
        #Resets board to original board
        self.sudoku_board = self.original_board
        self.set_original_sudoku()
        self.set_sudoku_backend()

    def is_full(self):
        #CHECK IF ALL CELLS HAVE VALUE
        for i in range(9):
            for j in range(9):
                if self.sudoku_board[i][j] == 0:
                    return False

        return True

    def update_board(self, x, y, value):
        #Board not updating right
        #Updates backend of board to the current user input board
        """
        Switched x and y for self.sudoku_board
        Dont know why
        """

        #CHANGE
        self.sudoku_board[y][x] = value
        Cell.set_cell_value(self.sudoku_backend[x][y], value)


    def find_empty(self):
        #searches through board and checks if it is empty
        for count in range(len(self.sudoku_board)):
            for i in range(len(self.sudoku_board[count])):
                if self.sudoku_board[count][i] == 0:
                    return count, i
        return None

    def check_board(self):
        #Checks if board is solved correctly
        for row in range(9):
            for col in range(9):
                row_copy = row
                col_copy = col
                while row_copy != 0:
                    if row_copy % 3 == 0:
                        break
                    row_copy -= 1
                while col_copy != 0:
                    if col_copy % 3 == 0:
                        break
                    col_copy -= 1
                # Cols is working rows is not
                # Cols are valid when generating values
                if self.valid_in_row(row, self.sudoku_board[row][col]) is True:
                    if self.valid_in_col(col, self.sudoku_board[row][col]) is True:
                        if self.valid_in_box(row_copy, col_copy, self.sudoku_board[row][col]) is True:
                            pass
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

        return True


    #Checker Functions
    def valid_in_box(self, row_start, col_start, num):
        counter = 0
        #Works
        row_start = int(row_start)
        col_start = int(col_start)
        for i in range(row_start, row_start + 3):
            for p in range(col_start, col_start + 3):
                if num == self.sudoku_board[i][p]:
                    counter += 1
                    if counter == 2:
                        return False
        return True

    def valid_in_col(self, col, num):
        counter = 0
        for count in range(len(self.sudoku_board)):
            if num == self.sudoku_board[count][col]:
                counter += 1
                if counter == 2:
                    return False
        return True

    def valid_in_row(self, row, num):
        counter = 0
        #CHECK IF IT WORKS??
        for count in range(len(self.sudoku_board[row])):
            if num == self.sudoku_board[row][count]:
                counter += 1
                if counter == 2:
                    return False
        return True

    def draw_border(self):
        color = (0, 0, 0)
        for i in range(0, 720, 240):
            for j in range(0, 720, 240):
                pygame.draw.line(self.screen, color,
                         (i + 80, j + 80),
                         (i + 320, j + 80), 7)

                pygame.draw.line(self.screen, color,
                         (i + 320, j + 80),
                         (i + 320, j + 320), 7)

                pygame.draw.line(self.screen, color,
                         (i + 320, j + 320),
                         (i + 80, j + 320), 7)

                pygame.draw.line(self.screen, color,
                         (i + 80, j + 320),
                         (i + 80, j + 80), 7)