from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random

class Cell(str, Enum):
  EMPTY = " "
  BLOCKED = "X"
  START = "S"
  GOAL = "G"
  PATH = "*"

class MazeLocation(NamedTuple):
  row: int
  column: int

class Maze:
  def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(9 ,9)):
    self._rows: int = rows
    self._columns: int = columns
    self.start: MazeLocation = start
    self.goal: MazeLocation = goal
    # fill the maze with empty cells
    self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
    # fill the maze with blocked cells
    self._randomly_fill(rows, columns, sparseness)
    # fill initial and final positions
    self._grid[start.row][start.column] = Cell.START
    self._grid[goal.row][goal.column] = Cell.GOAL
  
  def _randomly_fill(self, rows: int, columns: int, sparseness: float):
    for row in range(rows):
      for column in range(columns):
        if random.uniform(0, 1.0) < sparseness:
          self._grid[row][column] = Cell.BLOCKED

  def __str__(self):
    output: str = ""
    for row in self._grid:
      output += "".join([c.value for c in row]) + "\n"
    return output

  def goal_test(self, ml: MazeLocation):
    return self.goal == ml

  def sucessors(self, ml: MazeLocation):
    locations: List[MazeLocation] = []
    # check next row
    if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
      locations.append(MazeLocation(ml.row + 1, ml.column))
    # check previous row
    if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
      locations.append(MazeLocation(ml.row - 1, ml.column))
    # check next column
    if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
      locations.append(MazeLocation(ml.row, ml.column + 1))
    # check previous column
    if ml.column -1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
      locations.append(MazeLocation(ml.row, ml.column - 1))
    return locations

maze: Maze = Maze()
print(maze)
