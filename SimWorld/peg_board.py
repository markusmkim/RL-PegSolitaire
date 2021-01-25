from SimWorld.helpers import create_diamond_grid, create_triangle_grid


class PegBoard:

    def __init__(self, size, is_diamond, empty_nodes):

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

    # Executes the provided move on the current board
    def execute_move(self, move):
        self.grid[move[0][0]][move[0][1]] = 0
        self.grid[move[1][0]][move[1][1]] = 0
        self.grid[move[2][0]][move[2][1]] = 1
        self.total_pegs_left -= 1
