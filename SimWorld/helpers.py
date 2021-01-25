

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


# Returns the next state of the board after the provided action is taken. State is string.
def next_state(state, action):
    grid = convert_string_to_list(state)
    move = convert_string_to_list(action)
    grid[move[0][0]][move[0][1]] = 0
    grid[move[1][0]][move[1][1]] = 0
    grid[move[2][0]][move[2][1]] = 1
    return convert_list_to_string(grid)


# Used to convert list representations of states and actions to string representations
def convert_list_to_string(lst):
    s = ""
    for row in lst:
        for element in row:
            s += str(element)
        s += ","
    return s[:-1]


# Used to convert string representations of states and actions to list representations
def convert_string_to_list(string):
    lst = []
    rows = string.split(",")
    for row_string in rows:
        row = []
        for element in row_string:
            row.append(int(element))
        lst.append(row)
    return lst


# Returns all possible actions for the current board
def get_possible_actions(state):
    grid = convert_string_to_list(state)
    possible_actions = []
    size = len(grid)

    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                if len(grid[0]) > 1:  # Grid is diamond shaped

                    # Direction: up
                    if i > 1 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                        possible_actions.append(
                            str(i) + str(j) + "," + str(i - 1) + str(j) + "," + str(i - 2) + str(j))

                    # Direction: right
                    if j < size - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                        possible_actions.append(
                            str(i) + str(j) + "," + str(i) + str(j + 1) + "," + str(i) + str(j + 2))

                else:  # Grid is triangle shaped

                    # Direction: up
                    if i > 1 and j < len(grid[i]) - 2 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                        possible_actions.append(
                            str(i) + str(j) + "," + str(i - 1) + str(j) + "," + str(i - 2) + str(j))

                    # Direction: right
                    if i > 1 and j < len(grid[i]) - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                        possible_actions.append(
                            str(i) + str(j) + "," + str(i) + str(j + 1) + "," + str(i) + str(j + 2))

                # Direction: down & right
                if i < size - 2 and j < size - 2 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 0:
                    possible_actions.append(
                        str(i) + str(j) + "," + str(i + 1) + str(j + 1) + "," + str(i + 2) + str(j + 2))

                # Direction: down
                if i < size - 2 and grid[i + 1][j] == 1 and grid[i + 2][j] == 0:
                    possible_actions.append(
                        str(i) + str(j) + "," + str(i + 1) + str(j) + "," + str(i + 2) + str(j))

                # Direction: left
                if j > 1 and grid[i][j - 1] == 1 and grid[i][j - 2] == 0:
                    possible_actions.append(
                        str(i) + str(j) + "," + str(i) + str(j - 1) + "," + str(i) + str(j - 2))

                # Direction: up & left
                if i > 1 and j > 1 and grid[i - 1][j - 1] == 1 and grid[i - 2][j - 2] == 0:
                    possible_actions.append(
                        str(i) + str(j) + "," + str(i - 1) + str(j - 1) + "," + str(i - 2) + str(j - 2))

    return possible_actions


def get_all_possible_states(is_diamond, size):
    states = []
    if is_diamond:
        number_of_holes = size**2
    else:
        number_of_holes = (size * (size + 1)) / 2

    for i in range(2**number_of_holes):
        binary_number = bin(i).split("b")[-1]
        zeroes_padding = "0" * (number_of_holes - i)
        states += zeroes_padding + str(binary_number)

    return states


# Forms a spanning tree, with states as nodes and actions as edges. Returns the spanning tree as an 1D array
def get_all_possible_states_from_initial_state(initial_state):
    visited_nodes = {initial_state: True}
    tree = [initial_state]
    edges_to_explore = []
    current_node = initial_state
    edges = get_possible_actions(current_node)

    for edge in edges:
        edges_to_explore.append((current_node, edge))  # each tuple in list is node-edge (directed) pair

    while len(edges_to_explore) > 0:
        # print(edges_to_explore)
        node_edge_pair = edges_to_explore.pop(0)
        current_node = node_edge_pair[0]
        edge_to_traverse = node_edge_pair[1]

        new_node = next_state(current_node, edge_to_traverse)

        if new_node not in visited_nodes:
            # print(len(visited_nodes))
            visited_nodes[new_node] = True
            tree.append(new_node)
            new_edges = get_possible_actions(new_node)

            for edge in new_edges:
                edges_to_explore.append((new_node, edge))

    return tree  # list(set(tree))
