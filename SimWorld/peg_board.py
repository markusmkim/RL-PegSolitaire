from SimWorld.helpers import create_diamond_grid, create_triangle_grid


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

    # Executes the provided action on the current board
    def execute_action(self, action):
        self.grid[action[0][0]][action[0][1]] = 0
        self.grid[action[1][0]][action[1][1]] = 0
        self.grid[action[2][0]][action[2][1]] = 1
        self.total_pegs_left -= 1


