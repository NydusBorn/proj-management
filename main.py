import grid

if __name__ == "__main__":
    grid_cur = grid.grid(45, 131)
    grid_cur.carve_passages_from(1,1)
    print(grid_cur.__str__())
