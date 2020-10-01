# -*- coding: UTF-8 -*-

from enum import Enum

class SudokuCellValue(Enum):

    EMPTY = 0
    DIGIT1 = 1
    DIGIT2 = 2
    DIGIT3 = 3
    DIGIT4 = 4
    DIGIT5 = 5
    DIGIT6 = 6
    DIGIT7 = 7
    DIGIT8 = 8
    DIGIT9 = 9

class SudokuCell():

    def __init__(self, row, col, val = SudokuCellValue.EMPTY):
        self._row = row
        self._col = col
        self.val = val

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def block(self):
        return self._row // 3 * 3 + self._col // 3

    def __repr__(self):
        if self.val == SudokuCellValue.EMPTY:
            return " "
        return str(self.val.value)

class Sudoku():

    def __init__(self):
        self._numberOfRows = 9
        self._numberOfCols = 9
        self.cells = [[SudokuCell(row, col) for col in range(self._numberOfCols)] for row in range(self._numberOfRows)]

    @property
    def numberOfRows(self):
        return self._numberOfRows

    @property
    def numberOfCols(self):
        return self._numberOfCols

    def __repr__(self):
        breakline = "-" * (4 * self._numberOfCols + 1)
        output = breakline + "\n"
        for row in range(self._numberOfRows):
            for col in range(self._numberOfCols):
                textToAppend = ("| " + str(self.cells[row][col]) + " ") if col % 3 == 0 else ("  " + str(self.cells[row][col]) + " ")
                output += textToAppend
            textToAppend = ("|\n" + breakline + "\n") if row % 3 == 2 else "|\n"
            output += textToAppend
        return output

    def getCell(self, row, col):
        if not 0 <= row < self._numberOfRows:
            raise Exception("Invalid Sudoku Row")
        if not 0 <= col < self._numberOfCols:
            raise Exception("Invalid Sudoku Col")
        return self.cells[row][col]

    def setCell(self, cell):
        if not 0 <= cell.row < self._numberOfRows:
            raise Exception("Invalid Sudoku Row")
        if not 0 <= cell.col < self._numberOfCols:
            raise Exception("Invalid Sudoku Col")
        self.cells[cell.row][cell.col] = cell

