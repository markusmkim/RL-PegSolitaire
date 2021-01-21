

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


# Returns a list of all target node coordinates, assumed to be in the middle of the board
def find_target_nodes(size, is_diamond):
    if is_diamond:
        if size % 2 == 0:
            return [
                [size / 2 - 1, size / 2 - 1],
                [size / 2 - 1, size / 2],
                [size / 2, size / 2 - 1],
                [size / 2, size / 2],
            ]
        else:
            return [[(size - 1) / 2, (size - 1) / 2]]
    else:
        target_nodes_for_every_size = {
            4: [[2, 1]],
            5: [[2, 1], [3, 1], [3, 2]],
            6: [[3, 1], [3, 2], [4, 2]],
            7: [[4, 2]],
            8: [[4, 2], [5, 2], [5, 3]]
        }
        return target_nodes_for_every_size[size]


class PegBoard:

    def __init__(self, size, is_diamond, empty_nodes, target_nodes=False):

        # The size of the board is decided by the number of nodes at each edge of the board,
        # and ranges from 4 to 8 for triangles and 3 to 6 for diamonds by the task description
        self.size = size

        # Decides the shape of the board, where the shape is either diamond or triangle
        self.isDiamond = is_diamond

        # The grid is a list of lists of nodes representing the board as a coordinate system, where a
        # node value of 1 represents a peg, while a node value of 0 represents an empty node (hole)
        if is_diamond:
            self.grid = create_diamond_grid(size, empty_nodes)
            self.total_pegs_left = (size - 1) * (size - 1) - len(empty_nodes)
        else:
            self.grid = create_triangle_grid(size, empty_nodes)
            self.total_pegs_left = (size * (size + 1)) / 2 - len(empty_nodes)

        # For a game of solitaire to be won, the final peg must end up in on of the target nodes
        if target_nodes:
            self.target_nodes = target_nodes
        else:
            self.target_nodes = find_target_nodes(size, is_diamond)

    # Returns all possible actions for the current board
    def all_possible_actions(self):
        possible_actions = []
        grid = self.grid
        size = self.size

        if self.isDiamond:
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

        return possible_actions

    # Executes the provided action on the current board
    def execute_action(self, action):
        self.grid[action[0][0]][action[0][1]] = 0
        self.grid[action[1][0]][action[1][1]] = 0
        self.grid[action[2][0]][action[2][1]] = 1
        self.total_pegs_left -= 1

    # Needed to determine if a game of solitaire is won
    def target_nodes_contain_peg(self):
        for node in self.target_nodes:
            if self.grid[node[0]][node[1]] == 1:
                return True
        return True

    # Returns the next state of the board after the provided action is taken
    # def next_state(self, action):
    #     grid = self.grid.copy()
    #     grid[action[0][0]][action[0][1]] = 0
    #     grid[action[1][0]][action[1][1]] = 0
    #     grid[action[2][0]][action[2][1]] = 1
    #     return grid

    def print_board(self):
        for i in range(self.size):
            print(self.grid[i])
