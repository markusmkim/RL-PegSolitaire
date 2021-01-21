import networkx as nx
import matplotlib.pyplot as plt


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

    def visualize_board(self):
        if self.isDiamond:
            G = nx.Graph()
            blue_nodes = []
            red_nodes = []
            positions = {}

            # Add nodes
            for i in range(self.size):
                for j in range(self.size):

                    # Add node
                    G.add_node((i, j))

                    # Split filled/unfilled nodes into different lists to apply different colors
                    if self.grid[i][j] == 0:
                        blue_nodes.append((i, j))
                    else:
                        red_nodes.append((i, j))

                    # Add edges
                    if i > 0:
                        G.add_edge((i - 1, j), (i, j))
                    if j > 0:
                        G.add_edge((i, j - 1), (i, j))
                    if i > 0 and j > 0:
                        G.add_edge((i - 1, j - 1), (i, j))

                    # Add positions
                    positions[(i, j)] = (((i + j)*0.8), i - j)  # Works like coordinate system

            # add dummy nodes for scaling, stupid solution but it kind of works
            dummy_nodes = ['dummy_node_1', 'dummy_node_2']
            G.add_nodes_from(dummy_nodes)
            positions['dummy_node_1'] = (-1, 0)
            positions['dummy_node_2'] = ((self.size * 2) - 1, 0)

            # draw network
            nx.draw_networkx_nodes(G, positions, nodelist=blue_nodes, node_color='b')
            nx.draw_networkx_nodes(G, positions, nodelist=red_nodes, node_color='r')
            nx.draw_networkx_nodes(G, positions, nodelist=dummy_nodes, node_color='w')  # dummy nodes white -> invisible
            nx.draw_networkx_edges(G, positions)
            plt.show()

        else:
            G = nx.Graph()
            blue_nodes = []
            red_nodes = []
            positions = {}

            # Add nodes
            for i in range(self.size):
                for j in range(i + 1):

                    # Add node
                    G.add_node((i, j))

                    # Split filled/unfilled nodes into different lists to apply different colors
                    if self.grid[i][j] == 0:
                        blue_nodes.append((i, j))
                    else:
                        red_nodes.append((i, j))

                    # Add edges
                    if i > 0 and j < i:
                        G.add_edge((i - 1, j), (i, j))
                    if j > 0:
                        G.add_edge((i, j - 1), (i, j))
                    if i > 0 and j > 0:
                        G.add_edge((i - 1, j - 1), (i, j))

                    # Add positions
                    positions[(i, j)] = (((i + j) * 0.8), i - j)  # Works like coordinate system

            # draw network
            nx.draw_networkx_nodes(G, positions, nodelist=blue_nodes, node_color='b')
            nx.draw_networkx_nodes(G, positions, nodelist=red_nodes, node_color='r')
            nx.draw_networkx_edges(G, positions)
            plt.show()
