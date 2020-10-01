# -*- coding: UTF-8 -*-

import copy
import random
from sudoku import Sudoku, SudokuCellValue
from solver import SudokuSolver

class SudokuGenerator():

    def __init__(self, maxEmptyCells = 40):
        self.maxEmptyCells = maxEmptyCells

    def generate(self):

        # init an empty game
        emptyGame = Sudoku()

        # solve it randomly
        solver = SudokuSolver(emptyGame, enableRandom = True)
        solution = solver.sudoku

        # choose the cells to cleanup randomly
        cellIndices = random.sample(range(solution.numberOfRows * solution.numberOfCols), self.maxEmptyCells)

        # init the generated game as solution
        generatedGame = copy.deepcopy(solution)

        # iteratively try pop the cells
        for cellIndex in cellIndices:

            # get the cell using index and backup value
            cell = generatedGame.getCell(cellIndex // generatedGame.numberOfCols, cellIndex % generatedGame.numberOfCols)
            valueToBackup = cell.val

            # replace the value with SudokuCellValue.EMPTY
            cell.val = SudokuCellValue.EMPTY

            # if the solution is not unique after SudokuCellValue.EMPTY is filled, just simply revert the action
            if not SudokuSolver(generatedGame).isSolutionUnique:
                cell.val = valueToBackup

        # return the game and solution
        return (generatedGame, solution)

