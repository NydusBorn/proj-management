import time
import grid


def dfs_solution(grid_cur: grid.grid):
    start_time = time.time()
    start_point = (1, 1)
    end_point = (grid_cur.rows - 2, grid_cur.cols - 2)
    stack = [start_point]
    visited = set([start_point])
    parent = {start_point: None}  # Словарь для хранения родителей
    
    while stack:
        current_point = stack[-1]  # Берем последний элемент в стеке (текущая точка)
        
        # Если дошли до конца, восстанавливаем путь
        if current_point == end_point:
            path = []
            while current_point is not None:
                path.append(current_point)
                current_point = parent[current_point]  # Переходим к родительской клетке
            path.reverse()  # Путь нужно инвертировать, чтобы он был от старта до финиша
            for px, py in path:
                grid_cur.grid[px][py] = 2  # Помечаем путь
            return (len(path), time.time() - start_time)
        
        x, y = current_point
        neighbors = []
        
        # Проверяем соседей (вверх, вниз, влево, вправо)
        if x > 1 and grid_cur.grid[x - 1][y] == 0 and (x - 1, y) not in visited:
            neighbors.append((x - 1, y))
        if x < grid_cur.rows - 2 and grid_cur.grid[x + 1][y] == 0 and (x + 1, y) not in visited:
            neighbors.append((x + 1, y))
        if y > 1 and grid_cur.grid[x][y - 1] == 0 and (x, y - 1) not in visited:
            neighbors.append((x, y - 1))
        if y < grid_cur.cols - 2 and grid_cur.grid[x][y + 1] == 0 and (x, y + 1) not in visited:
            neighbors.append((x, y + 1))
        
        if not neighbors:
            # Если нет доступных соседей (тупик), откатываемся назад
            stack.pop()  # Удаляем текущую точку из стека
        else:
            # Если есть соседи, выбираем одного и продолжаем
            next_point = neighbors[0]  # Можно выбрать любой сосед
            stack.append(next_point)
            visited.add(next_point)
            parent[next_point] = current_point  # Сохраняем информацию о родителе
    
    return (None, time.time() - start_time)



def greedy_solution(grid_cur: grid.grid):
    start_time = time.time()
    current_point = (1,1)
    end_point = (grid_cur.rows - 2, grid_cur.cols - 2)
    point_stack = [current_point]
    visited = set([current_point])
    while current_point != end_point:
        possible_points = []
        if current_point[0] > 1 and grid_cur.grid[current_point[0] - 1][current_point[1]] != 1 and not visited.__contains__((current_point[0] - 1, current_point[1])):
            possible_points.append((current_point[0] - 1, current_point[1]))
        if current_point[0] < grid_cur.rows - 2 and grid_cur.grid[current_point[0] + 1][current_point[1]] != 1 and not visited.__contains__((current_point[0] + 1, current_point[1])):
            possible_points.append((current_point[0] + 1, current_point[1]))
        if current_point[1] > 1 and grid_cur.grid[current_point[0]][current_point[1] - 1] != 1 and not visited.__contains__((current_point[0], current_point[1] - 1)):
            possible_points.append((current_point[0], current_point[1] - 1))
        if current_point[1] < grid_cur.cols - 2 and grid_cur.grid[current_point[0]][current_point[1] + 1] != 1 and not visited.__contains__((current_point[0], current_point[1] + 1)):
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
