from operator import ne
from threading import currentThread
import time
import grid

states = {
        "void": 0,
        "wall": 1,
        "path": 2
    }
def BFS(grid) :
    start_time = time.time()
    start = (1, 1)
    end = (grid.rows - 2, grid.cols - 2)

    grid.grid[start[0]][start[1]] = 2
    queue = [start]
    visited=[start]
    path = {}
    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in [(current[0] + 1, current[1]), (current[0] - 1, current[1]), (current[0], current[1] + 1), (current[0], current[1] - 1)]:
            if neighbor in visited:
                continue
            if grid.grid[neighbor[0]][neighbor[1]] == states["void"]:
                queue.append(neighbor)
                visited.append(neighbor)
                path[neighbor] = current
    current=end
    while current!=start:
        grid.grid[current[0]][current[1]] = 2
        current=path[current]

    end_time = time.time()
    
    return {"time": end_time - start_time, "length": len(path)}
    
    
   

