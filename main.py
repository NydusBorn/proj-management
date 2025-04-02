import grid
import solvers

if __name__ == "__main__":
    grid_cur = grid.grid(45, 135)
    grid_cur.carve_passages_from(1, 1)
    solution = solvers.dfs_solution(grid_cur)
    print(f"Path length: {solution[0]}")
    print(f"Time spent: {solution[1]}s")
    print(grid_cur.__str__())
    grid_cur.clear_path()
    grid_cur = grid.grid(45, 131)
    grid_cur.carve_passages_from(1,1)

    solution = solvers.greedy_solution(grid_cur)
    print(f"Path length: {solution[0]}")
    print(f"Time spent: {solution[1]}s")
    print(grid_cur.__str__())
    grid_cur.clear_path()
    print(grid_cur.__str__())


