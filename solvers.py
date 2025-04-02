import time
import grid

def dfs_solution(grid_cur: grid.grid):
    start_time = time.time()
    start_point = (1, 1)
    end_point = (grid_cur.rows - 2, grid_cur.cols - 2)
    stack = [start_point]
    visited = set([start_point])
    path = []
    
    while stack:
        current_point = stack.pop()
        path.append(current_point)
        
        if current_point == end_point:
            for px, py in path:
                grid_cur.grid[px][py] = 2
            return (len(path), time.time() - start_time)
        
        x, y = current_point
        neighbors = []
        if x > 1 and grid_cur.grid[x - 1][y] == 0 and (x - 1, y) not in visited:
            neighbors.append((x - 1, y))
        if x < grid_cur.rows - 2 and grid_cur.grid[x + 1][y] == 0 and (x + 1, y) not in visited:
            neighbors.append((x + 1, y))
        if y > 1 and grid_cur.grid[x][y - 1] == 0 and (x, y - 1) not in visited:
            neighbors.append((x, y - 1))
        if y < grid_cur.cols - 2 and grid_cur.grid[x][y + 1] == 0 and (x, y + 1) not in visited:
            neighbors.append((x, y + 1))
        
        for neighbor in neighbors:
            stack.append(neighbor)
            visited.add(neighbor)
    
    return (None, time.time() - start_time)


grid_cur = grid.grid(45, 135)
grid_cur.carve_passages_from(1, 1)
solution = dfs_solution(grid_cur)
print(f"Path length: {solution[0]}")
print(f"Time spent: {solution[1]}s")
print(grid_cur.__str__())
