import networkx as nx
import matplotlib.pyplot as plt


class PegBoard:
    def __init__(self, size, isDiamond, empty_nodes):
        self.size = size
        self.isDiamond = isDiamond

        if isDiamond:
            self.grid = self.create_diamond_grid(size, empty_nodes)

        else:
            self.grid = self.create_triangle_grid(size, empty_nodes)



    def create_triangle_grid(self, size, empty_nodes):
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


    def create_diamond_grid(self, size, empty_nodes):
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


    def get_possible_actions(self):
        possible_actions = []
        grid = self.grid
        size = self.size

        if self.isDiamond:
            for i in range(size):
                for j in range(size):
                    if grid[i][j] == 1:
                        if i > 1 and grid[i - 1][j] == 1 and grid[i - 2][j] == 0:
                            possible_actions.append([[i, j], [i - 1, j], [i - 2, j]])

                        if j < size - 2 and grid[i][j + 1] == 1 and grid[i][j + 2] == 0:
                            possible_actions.append([[i, j], [i, j + 1], [i, j + 2]])

                        if i < size - 2 and j < size - 2 and grid[i + 1][j + 1] == 1 and grid[i + 2][j + 2] == 0:
                            possible_actions.append([[i, j], [i + 1, j + 1], [i + 2, j + 2]])

                        if i < size - 2 and grid[i + 1][j] == 1 and grid[i + 2][j] == 0:
                            possible_actions.append([[i, j], [i + 1, j], [i + 2, j]])

                        if j > 1 and grid[i][j - 1] == 1 and grid[i][j - 2] == 0:
                            possible_actions.append([[i, j], [i, j - 1], [i, j - 2]])

                        if i > 1 and j > 1 and grid[i - 1][j - 1] == 1 and grid[i - 2][j - 2] == 0:
                            possible_actions.append([[i, j], [i - 1, j - 1], [i - 2, j - 2]])

        return possible_actions

    def execute_action(self, action):
        self.grid[action[0][0]][action[0][1]] = 0
        self.grid[action[1][0]][action[1][1]] = 0
        self.grid[action[2][0]][action[2][1]] = 1


    def print_board(self):
        for i in range(self.size):
            print(self.grid[i], i)


    def visualize_board(self):
        if self.isDiamond:
            G = nx.Graph()
            blue_nodes = []
            red_nodes = []
            positions = {}
            # Add nodes
            for i in range(self.size):
                for j in range(self.size):
                    # add node
                    G.add_node((i, j))

                    # split filled/unfilled nodes into different lists to apply different colors
                    if self.grid[i][j] == 0:
                        blue_nodes.append((i, j))
                    else:
                        red_nodes.append((i, j))

                    # add edges
                    if i > 0:
                        G.add_edge((i - 1, j), (i, j))
                    if j > 0:
                        G.add_edge((i, j - 1), (i, j))
                    if i > 0 and j > 0:
                        G.add_edge((i - 1, j - 1), (i, j))


                    # add positions
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

if __name__ == '__main__':
    board = PegBoard(6, True, [[3, 3]])

    print(board.print_board())



    print('Actions:')
    pa = board.get_possible_actions()
    for i in pa:
        print(i)

    action = [[1, 1], [2, 2], [3, 3]]
    print('Excecuting action, ', action)
    board.execute_action(action)

    board.print_board()

    board.visualize_board()





