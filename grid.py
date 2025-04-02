import random
class grid:
    def __init__(self, rows, cols):
        """
        Initialize a grid with the given number of rows and columns.
        :param rows:
        :param cols:
        cell with 0 - free cell
        cell with 1 - wall
        cell with 2 - path
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[1 for _ in range(cols)] for _ in range(rows)]
    def clear_path(self):
        # Convert all cells with a value of 2 to 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 2:
                    self.grid[r][c] = 0

    def carve_passages_from(self, r, c):
        # Directions: move two cells (vertical & horizontal) at a time.
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            # Avoid carving out-of-bound or into the border.
            if new_r < 1 or new_r > self.rows - 2 or new_c < 1 or new_c > self.cols - 2:
                continue
            # If the new cell is still a wall, carve through.
            if self.grid[new_r][new_c] == 1:
                # Remove the wall between the current cell and the neighbor.
                self.grid[r + dr // 2][c + dc // 2] = 0
                self.grid[new_r][new_c] = 0
                self.carve_passages_from(new_r, new_c)

    def __str__(self):
        # Create a string representation of the grid.
        # Here " " represents a free cell and "█" represents a wall.
        s = ""
        for row in self.grid:
            s += "".join(" " if cell == 0 else "." if cell == 2 else "█" for cell in row) + "\n"
        return s