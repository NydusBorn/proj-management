import grid
import solvers
if __name__ == "__main__":
    grid_cur = grid.grid(45, 135)
    grid_cur.carve_passages_from(1, 1)
    solution = solvers.BFS(grid_cur)
    print("BFS")
    print(f"Path length: {solution["length"]}")
    print(f"Time spent: {solution["time"]}s")
    print(grid_cur.__str__())
    grid_cur.clear_path()
    solution = solvers.dfs_solution(grid_cur)
    print("DFS")
    print(f"Path length: {solution[0]}")
    print(f"Time spent: {solution[1]}s")
    print(grid_cur.__str__())
    grid_cur.clear_path()
    solution = solvers.greedy_solution(grid_cur)
    print("Greedy")
    print(f"Path length: {solution[0]}")
    print(f"Time spent: {solution[1]}s")
    print(grid_cur.__str__())

