from xml.etree.ElementTree import tostring

import grid

if __name__ == "__main__":
    grid_cur = grid.grid(11, 11)
    grid_cur.carve_passages_from(1,1)
    print(grid_cur.__str__())
