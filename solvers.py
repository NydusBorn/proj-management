import time
import grid
def greedy_solution(grid_cur: grid.grid):
    start_time = time.time()
    current_point = (1,1)
    end_point = (grid_cur.rows - 2, grid_cur.cols - 2)
    point_stack = [current_point]
    visited = set([current_point])
    while current_point != end_point:
        possible_points = []
        if current_point[0] > 1 and grid_cur.grid[current_point[0] - 1][current_point[1]] == 0 and not visited.__contains__((current_point[0] - 1, current_point[1])):
            possible_points.append((current_point[0] - 1, current_point[1]))
        if current_point[0] < grid_cur.rows - 2 and grid_cur.grid[current_point[0] + 1][current_point[1]] == 0 and not visited.__contains__((current_point[0] + 1, current_point[1])):
            possible_points.append((current_point[0] + 1, current_point[1]))
        if current_point[1] > 1 and grid_cur.grid[current_point[0]][current_point[1] - 1] == 0 and not visited.__contains__((current_point[0], current_point[1] - 1)):
            possible_points.append((current_point[0], current_point[1] - 1))
        if current_point[1] < grid_cur.cols - 2 and grid_cur.grid[current_point[0]][current_point[1] + 1] == 0 and not visited.__contains__((current_point[0], current_point[1] + 1)):
            possible_points.append((current_point[0], current_point[1] + 1))
        if not possible_points:
            current_point = point_stack.pop()
            continue
        heuristic = lambda x: abs(x[0] - end_point[0]) + abs(x[1] - end_point[1])
        current_point = min(possible_points, key=heuristic)
        point_stack.append(current_point)
        visited.add(current_point)
    for point in point_stack:
        grid_cur.grid[point[0]][point[1]] = 2
    return (len(point_stack), time.time() - start_time)
