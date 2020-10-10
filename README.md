## #️⃣ Sudoku Generator

![python](https://img.shields.io/badge/python-3+-blue.svg)
![dependency](https://img.shields.io/badge/dependency-none-green.svg)
![etc](https://img.shields.io/badge/etc-few%20seconds-yellow.svg)
![license](https://img.shields.io/badge/license-none-blueviolet.svg)

Randomly generate a sudoku game and output its solution as well. It is guaranteed that there is EXACTLY ONE possible solution.


### 📔 Usage

Clone or download the scripts from the repository. Import the modules and that's all:

```python
# example.py

from sudoku import Sudoku, SudokuCell, SudokuCellValue
from generator import SudokuGenerator

generator = SudokuGenerator(maxEmptyCells = 50)
(game, solution) = generator.generate()

print(game)
print(solution)
```

![Imgur](https://i.imgur.com/LurZnAE.png)


### 📝 Interfaces

[sudoku.py](https://github.com/der3318/sudoku-generator/blob/master/sudoku.py) contains all the basic interfaces.

| Class | Attribute | Description |
| :- | :- | :- |
| SudokuCellValue | Enum | digits of a cell including SudokuCellValue.EMPTY, DIGIT1, etc. |
| SudokuCell | row/col/block | returns a integer from 0 to 8 to describe the position of the cell |
| SudokuCell | val | returns the corresponding SudokuCellValue of the cell |
| Sudoku | numberOfRows/numberOfCols | should be integer 9 |
| Sudoku | getCell(row, col) | returns the reference to the cell at the position or raises an exception |
| Sudoku | setCell(cell) | updates the Sudoku game using this SudokuCell |

Both game and solution are an instances of Sudoku. Here is a short example:

```python
cell = game.getCell(8, 0)                 # get the cell at the bottom left corner from generated game
print(cell.block)                         # should be 6
print(cell.val == SudokuCellValue.EMPTY)  # should be TRUE

cell = solution.getCell(8, 0)             # get the cell at the bottom left corner from its solution
print(cell.val == SudokuCellValue.DIGIT6) # should be TRUE
```


### 🔑 Implementation

The idea is pretty simple without any fancy algorithm. First of all, what we need is a quick (best hypothesis based BFS) and powerful [sudoku solver](https://github.com/der3318/sudoku-generator/blob/master/solver.py) having the ability to:

| Property | Description |
| :- | :- |
| SudokuSolver.__trySolve(sudoku) | tries to solve the game randomly |
| SudokuSolver.doesSolutionExist | indicates whether it can find a solution |
| SudokuSolver.isSolutionUnique | indicates whether the solution is unique |

Then, we initialize the game with an empty borad in [sudoku generator](https://github.com/der3318/sudoku-generator/blob/master/generator.py) and solve it using the above solver. This is the solution we are going to return.

The last thing required is to iteratively pop a random cell from the solution. In each round, the poped result should be tested and make sure it still has only one solution. Otherwise, the cell is considered kept.

