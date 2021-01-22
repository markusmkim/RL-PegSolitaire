import networkx as nx
import matplotlib.pyplot as plt

def visualize_board(grid):
    if len(grid[0]) > 1:  # is diamond shaped
        G = nx.Graph()
        blue_nodes = []
        red_nodes = []
        positions = {}

        # Add nodes
        for i in range(len(grid)):
            for j in range(len(grid)):

                # Add node
                G.add_node((i, j))

                # Split filled/unfilled nodes into different lists to apply different colors
                if grid[i][j] == 0:
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
                positions[(i, j)] = (((i + j) * 0.8), i - j)  # Works like coordinate system

        # add dummy nodes for scaling, stupid solution but it kind of works
        dummy_nodes = ['dummy_node_1', 'dummy_node_2']
        G.add_nodes_from(dummy_nodes)
        positions['dummy_node_1'] = (-1, 0)
        positions['dummy_node_2'] = ((len(grid) * 2) - 1, 0)

        # draw network
        nx.draw_networkx_nodes(G, positions, nodelist=blue_nodes, node_color='b')
        nx.draw_networkx_nodes(G, positions, nodelist=red_nodes, node_color='r')
        nx.draw_networkx_nodes(G, positions, nodelist=dummy_nodes, node_color='w')  # dummy nodes white -> invisible
        nx.draw_networkx_edges(G, positions)
        plt.show()

    else:  # is triangle shaped
        G = nx.Graph()
        blue_nodes = []
        red_nodes = []
        positions = {}

        # Add nodes
        for i in range(len(grid)):
            for j in range(i + 1):

                # Add node
                G.add_node((i, j))

                # Split filled/unfilled nodes into different lists to apply different colors
                if grid[i][j] == 0:
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