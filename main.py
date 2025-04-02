import grid
from solvers import *

if __name__ == "__main__":
    grid_cur = grid.grid(45, 131)
    grid_cur.carve_passages_from(1,1)
    solution = BFS(grid_cur)

    print(f'Time: {solution["time"]}\nLength: {solution["length"]}')
    print(grid_cur.__str__())

