import networkx as nx

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
    e = [(1, 2), (2, 3), (3, 4)]  # list of edges
    meadow = nx.Graph(e)  # or DiGraph, MultiGraph, MultiDiGraph, etc
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

    #
    print(f'meadow.nodes[0]["attr1"]={meadow.nodes[2]["is_meadow"]}')

    # meadow=nx.path_graph(8)
    # meadow.add_edge(0, 5)
    # meadow.add_edge(0, 6)
    # meadow.add_edge(0, 7)

    # meadow.add_edge(1, 2)
    # meadow.add_edge(1, 3)
    # meadow.add_edge(1, 4)
    return meadow


def create_road():
    road = nx.path_graph(4)
    road.add_edge(0, 2)
    return road


def create_town():
    town = nx.path_graph(4)
    town.add_edge(0, 2)
    return town
