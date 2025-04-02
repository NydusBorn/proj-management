
class grid:
    def __init__(self, rows, cols):
        """
        Initialize a grid with the given number of rows and columns.
        :param rows:
        :param cols:
        cell with 0 - free cell
        cell with 1 - wall
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]