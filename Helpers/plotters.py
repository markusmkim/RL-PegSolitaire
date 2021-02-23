import networkx as nx
import matplotlib.pyplot as plt


class BoardVisualizer:
    def __init__(self, output_path):
        self.output_path = output_path
        self.current_move = 0


    def visualize_board(self, grid):
        G = nx.Graph()
        blue_nodes = []
        red_nodes = []
        positions = {}

        # Add nodes
        for i in range(len(grid)):
            for j in range(len(grid) if len(grid[0]) > 1 else i + 1):

                # Add node
                G.add_node((i, j))

                # Split filled/unfilled nodes into different lists to apply different colors
                if grid[i][j] == 0:
                    blue_nodes.append((i, j))
                else:
                    red_nodes.append((i, j))

                # Add edges
                if len(grid[0]) > 1:  # Grid is diamond shaped
                    if i > 0:
                        G.add_edge((i - 1, j), (i, j))
                else:  # Grid is triangle shaped
                    if i > 0 and j < i:
                        G.add_edge((i - 1, j), (i, j))
                if j > 0:
                    G.add_edge((i, j - 1), (i, j))
                if i > 0 and j > 0:
                    G.add_edge((i - 1, j - 1), (i, j))

                # Add positions
                positions[(i, j)] = (((i + j) * 0.8), i - j)  # Works like a coordinate system

        # Add dummy nodes for visual scaling
        if len(grid[0]) > 1:
            dummy_nodes = ['dummy_node_1', 'dummy_node_2']
            G.add_nodes_from(dummy_nodes)
            positions['dummy_node_1'] = (-2, 0)
            positions['dummy_node_2'] = ((len(grid) * 2) - 2, 0)
            nx.draw_networkx_nodes(G, positions, nodelist=dummy_nodes, node_color='w')  # Dummy nodes are white/invisible

        # Draw network
        nx.draw_networkx_nodes(G, positions, nodelist=blue_nodes, node_color='b')
        nx.draw_networkx_nodes(G, positions, nodelist=red_nodes, node_color='r')
        nx.draw_networkx_edges(G, positions)

        if self.output_path is not None:
            filepath = self.output_path + 'plots_last_episode/' + str(self.current_move)
            plt.savefig(filepath)
        plt.show()
        self.current_move += 1


def plot_mean_values(values, output_path=None):
    x_axis = []
    mean_values = []

    for i in range(len(values) // 100):
        mean = 0
        for j in range(100):
            mean += values[i*100 + j]
        mean_values.append(mean/100)

    for i in range(len(mean_values)):
        x_axis.append(i)

    plt.plot(x_axis, mean_values)
    if output_path is not None:
        filepath = output_path + 'average_pegs_left'
        plt.savefig(filepath)
    plt.show()


def plot_values(values, output_path=None):
    x_axis = []
    for i in range(len(values)):
        x_axis.append(i)
    plt.plot(x_axis, values)
    if output_path is not None:
        filepath = output_path + 'pegs_left'
        plt.savefig(filepath)
    plt.show()
