from Helpers.converters import convert_list_to_string, convert_string_to_list


# Returns the next state of the board after the provided action is taken. State is string.
def next_state(state, action):
    grid = convert_string_to_list(state)
    move = convert_string_to_list(action)
    grid[move[0][0]][move[0][1]] = 0
    grid[move[1][0]][move[1][1]] = 0
    grid[move[2][0]][move[2][1]] = 1
    return convert_list_to_string(grid)


# Returns all possible actions for the current board
def get_possible_actions(state):
    grid = convert_string_to_list(state)
    possible_actions = []
    size = len(grid)

    for i in range(size):
        for j in range(size if len(grid[0]) > 1 else i + 1):
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

