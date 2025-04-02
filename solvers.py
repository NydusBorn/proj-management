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


