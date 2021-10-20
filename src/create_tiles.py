import networkx as nx
import matplotlib.pyplot as plt

"""
Object representing Tile

"""


def add_two(self, x):
    return x + 2


def create_tiles():
    pass


def create_tile():
    pass


def create_meadow():
    # Create graph for tile to represent meadow connections in tile.
    # Index 0 =top left half edge of tile, counts clockwise positive
    meadow = nx.Graph()
    meadow.add_nodes_from(range(0, 8))

    # Specify the connections of the meadow in the tile.
    meadow.add_edge(0, 5)
    meadow.add_edge(0, 6)
    meadow.add_edge(0, 7)
    meadow.add_edge(1, 2)
    meadow.add_edge(1, 3)
    meadow.add_edge(1, 4)
    meadow.add_edge(2, 3)
    meadow.add_edge(2, 4)
    meadow.add_edge(3, 4)
    meadow.add_edge(5, 6)
    meadow.add_edge(5, 7)
    meadow.add_edge(6, 7)

    # Specify each of the 8 nodes on the edge of the tile, is a meadow or not.
    attrs = {
        0: {"is_meadow": True},
        1: {"is_meadow": True},
        2: {"is_meadow": True},
        3: {"is_meadow": True},
        4: {"is_meadow": True},
        5: {"is_meadow": True},
        6: {"is_meadow": True},
        7: {"is_meadow": True},
    }
    nx.set_node_attributes(meadow, attrs)

    # plot the meadow graph
    plot_graph(meadow)
    return meadow


def create_road():
    # Create graph for tile to represent road connections in tile.
    # Index 0 =top edge of tile, counts clockwise positive
    road = nx.Graph()
    road.add_nodes_from(range(0, 4))

    # Specify the connections of the road in the tile.
    road.add_edge(0, 2)

    # Specify each of the 8 nodes on the edge of the tile, is a road or not.
    attrs = {
        0: {"is_road": True},
        1: {"is_road": True},
        2: {"is_road": True},
        3: {"is_road": True},
    }
    nx.set_node_attributes(road, attrs)

    # plot the road graph
    plot_graph(road)
    return road


def create_town():
    # Create graph for tile to represent town connections in tile.
    # Index 0 =top edge of tile, counts clockwise positive
    town = nx.Graph()
    town.add_nodes_from(range(0, 4))

    # Specify the connections of the town in the tile.
    town.add_edge(0, 2)

    # Specify each of the 8 nodes on the edge of the tile, is a town or not.
    attrs = {
        0: {"is_town": True},
        1: {"is_town": True},
        2: {"is_town": True},
        3: {"is_town": True},
    }
    nx.set_node_attributes(town, attrs)

    # plot the town graph
    plot_graph(town)
    return town


def plot_graph(G):

    # explicitly set positions
    if G.number_of_nodes() == 4:
        pos = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
        plt.plot([-1, 1], [1, 1], "bo", linestyle="--")
        plt.plot([1, 1], [1, -1], "bo", linestyle="--")
        plt.plot([1, -1], [-1, -1], "bo", linestyle="--")
        plt.plot([-1, -1], [-1, 1], "bo", linestyle="--")
        plt.title("Road or Town")
    elif G.number_of_nodes() == 8:
        plt.plot([-2, 2], [2, 2], "bo", linestyle="--")
        plt.plot([2, 2], [2, -2], "bo", linestyle="--")
        plt.plot([2, -2], [-2, -2], "bo", linestyle="--")
        plt.plot([-2, -2], [-2, 2], "bo", linestyle="--")
        plt.title("Meadow")
        pos = {
            0: (-1, 2),
            1: (1, 2),
            2: (2, 1),
            3: (2, -1),
            4: (1, -2),
            5: (-1, -2),
            6: (-2, -1),
            7: (-2, 1),
        }

    options = {
        "font_size": 36,
        "node_size": 3000,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    nx.draw_networkx(G, pos, **options)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")

    plt.show()
