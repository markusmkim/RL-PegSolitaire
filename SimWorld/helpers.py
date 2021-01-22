import copy

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


# Returns the next state of the board after the provided action is taken
def next_state(state, action):
     grid = state.copy()
     grid[action[0][0]][action[0][1]] = 0
     grid[action[1][0]][action[1][1]] = 0
     grid[action[2][0]][action[2][1]] = 1
     return grid


# Returns all possible actions for the current board
def get_possible_actions(grid):
    possible_actions = []

    size = len(grid)

    # Checks if grid has diamond shape
    if len(grid[0]) > 1:
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 1:

                    # Direction: up
                    if i > 1 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                        possible_actions.append([[i, j], [i - 1, j], [i - 2, j]])

                    # Direction: right
                    if j < size - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                        possible_actions.append([[i, j], [i, j + 1], [i, j + 2]])

                    # Direction: down & right
                    if i < size - 2 and j < size - 2 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 0:
                        possible_actions.append([[i, j], [i + 1, j + 1], [i + 2, j + 2]])

                    # Direction: down
                    if i < size - 2 and grid[i + 1][j] == 1 and grid[i + 2][j] == 0:
                        possible_actions.append([[i, j], [i + 1, j], [i + 2, j]])

                    # Direction: left
                    if j > 1 and grid[i][j - 1] == 1 and grid[i][j - 2] == 0:
                        possible_actions.append([[i, j], [i, j - 1], [i, j - 2]])

                    # Direction: up & left
                    if i > 1 and j > 1 and grid[i - 1][j - 1] == 1 and grid[i - 2][j - 2] == 0:
                        possible_actions.append([[i, j], [i - 1, j - 1], [i - 2, j - 2]])

    else:
        for i in range(size):
            for j in range(i + 1):
                if grid[i][j] == 1:

                    # Direction: up
                    if i > 1 and j < len(grid[i]) - 2 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                        possible_actions.append([[i, j], [i - 1, j], [i - 2, j]])

                    # Direction: right
                    if i > 1 and j < len(grid[i]) - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                        possible_actions.append([[i, j], [i, j + 1], [i, j + 2]])

                    # Direction: down & right
                    if i < size - 2 and j < size - 2 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 0:
                        possible_actions.append([[i, j], [i + 1, j + 1], [i + 2, j + 2]])

                    # Direction: down
                    if i < size - 2 and grid[i + 1][j] == 1 and grid[i + 2][j] == 0:
                        possible_actions.append([[i, j], [i + 1, j], [i + 2, j]])

                    # Direction: left
                    if j > 1 and grid[i][j - 1] == 1 and grid[i][j - 2] == 0:
                        possible_actions.append([[i, j], [i, j - 1], [i, j - 2]])

                    # Direction: up & left
                    if i > 1 and j > 1 and grid[i - 1][j - 1] == 1 and grid[i - 2][j - 2] == 0:
                        possible_actions.append([[i, j], [i - 1, j - 1], [i - 2, j - 2]])

    return possible_actions


# Forms a spanning tree, with states as nodes and actions as edges. Returns the spanning tree as a 1D array
def get_all_possible_states_from_initial_state(initial_state):
    tree = [initial_state]
    edges_to_explore = []
    current_node = copy.deepcopy(initial_state)
    edges = get_possible_actions(current_node)
    for edge in edges:
        edges_to_explore.append((current_node, edge))  # each tuple in list is node-edge (directed) pair

    while len(edges_to_explore) > 0:
        node_edge_pair = edges_to_explore.pop(0)
        current_node = copy.deepcopy(node_edge_pair[0])
        edge_to_traverse = copy.deepcopy(node_edge_pair[1])

        new_node = copy.deepcopy(next_state(current_node, edge_to_traverse))

        if new_node not in tree:
            tree.append(new_node)
            new_edges = get_possible_actions(new_node)
            for edge in new_edges:
                edges_to_explore.append((new_node, edge))

    return tree
