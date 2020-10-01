# -*- coding: UTF-8 -*-

import copy
import random
from sudoku import SudokuCellValue

class BoardAnalyzer():

    def __init__(self, sudoku):

        # best cells to apply
        self.bestCellsToApply = None

        # compute restriction cache
        rowCacheSet, colCacheSet, blockCacheSet = set(), set(), set()
        for row in range(sudoku.numberOfRows):
            for col in range(sudoku.numberOfCols):
                if sudoku.getCell(row, col).val == SudokuCellValue.EMPTY:
                    continue
                (rowCache, colCache, blockCache) = self.__cellToCacheStrings(sudoku.getCell(row, col))
                rowCacheSet.add(rowCache)
                colCacheSet.add(colCache)
                blockCacheSet.add(blockCache)

        # find the empty cell having least possible values
        for row in range(sudoku.numberOfRows):
            for col in range(sudoku.numberOfCols):
                if sudoku.getCell(row, col).val != SudokuCellValue.EMPTY:
                    continue        # not an empty cell
                possibleCellList = list()
                for possibleValue in SudokuCellValue:
                    if possibleValue == SudokuCellValue.EMPTY:
                        continue    # try only DIGIT1 to DIGIT9
                    possibleCell = copy.deepcopy(sudoku.getCell(row, col))
                    possibleCell.val = possibleValue
                    (rowCache, colCache, blockCache) = self.__cellToCacheStrings(possibleCell)
                    if rowCache in rowCacheSet or colCache in colCacheSet or blockCache in blockCacheSet:
                        continue    # not applicable
                    possibleCellList.append(possibleCell)
                if self.bestCellsToApply is None or len(possibleCellList) < len(self.bestCellsToApply):
                    self.bestCellsToApply = possibleCellList

    def __cellToCacheStrings(self, cell):
        rowCache = str(cell.row) + ":" + str(cell.val.value)
        colCache = str(cell.col) + ":" + str(cell.val.value)
        blockCache = str(cell.block) + ":" + str(cell.val.value)
        return (rowCache, colCache, blockCache)


class SudokuSolver():

    def __init__(self, sudoku, enableRandom = False):
        self._doesSolutionExist = False
        self._isSolutionUnique = True
        self.sudoku = None
        self.__trySolve(sudoku, enableRandom)

    @property
    def doesSolutionExist(self):
        return self._doesSolutionExist

    @property
    def isSolutionUnique(self):
        return self._isSolutionUnique

    def __trySolve(self, sudoku, enableRandom):

        # init searching stack
        stack = list()
        stack.append(copy.deepcopy(sudoku))

        # start searching
        while stack:
            poppedSudoku = stack.pop()
            bestCellsToApply = BoardAnalyzer(poppedSudoku).bestCellsToApply
            if bestCellsToApply is None:        # solution found
                self._isSolutionUnique = (not self._doesSolutionExist)
                self._doesSolutionExist = True
                self.sudoku = poppedSudoku
            else:                               # apply possible cells and keep searching
                if enableRandom:
                    random.shuffle(bestCellsToApply)
                for cell in bestCellsToApply:
                    poppedSudoku.setCell(cell)
                    stack.append(copy.deepcopy(poppedSudoku))
            if not self._isSolutionUnique:      # stop searching once at least two solutions are found
                return

