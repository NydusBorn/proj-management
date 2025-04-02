import random
def generate_maze(grid, start, end):
    """
    Generate a maze using the recursive backtracking algorithm.
    :param grid: The grid object to generate the maze on.
    :param start: The starting point of the maze (x, y).
    :param end: The ending point of the maze (x, y).
    """
    def carve_path(x, y):
        grid.grid[y][x] = 0  # Mark the current cell as part of the path
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, down, left, right
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if (0 <= nx < grid.cols) and (0 <= ny < grid.rows) and grid.grid[ny][nx] == 1:
                grid.grid[ny - dy][nx - dx] = 0  # Carve a path to the next cell
                carve_path(nx, ny)

    # Initialize the grid with all walls
    for y in range(grid.rows):
        for x in range(grid.cols):
            grid.grid[y][x] = 1

    # Carve a path from the start to the end
    carve_path(start[0], start[1])

    # Mark the start and end points as part of the path
    grid.grid[start[1]][start[0]] = 0
    grid.grid[end[1]][end[0]] = 0