

# Static initializer of a triangle shaped grid
def create_triangle_grid(size, empty_nodes):
    grid = []
    for i in range(size):
        row = []
        for j in range(i + 1):
            if [i, j] in empty_nodes:
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid


# Static initializer of a diamond shaped grid
def create_diamond_grid(size, empty_nodes):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            if [i, j] in empty_nodes:
                row.append(0)
            else:
                row.append(1)
        grid.append(row)
    return grid
