import networkx as nx
"""
Object representing Tile

"""
def add_two(self, x):
    return x+2
    
def create_tiles():
    pass
    
def create_tile():
    pass

def create_meadow():
    meadow = nx.Graph()  # or DiGraph, MultiGraph, MultiDiGraph, etc
    meadow = nx.Graph(name="Freek")
    e = [(1, 2), (2, 3), (3, 4)]  # list of edges
    meadow = nx.Graph(e)
    #meadow=nx.path_graph(8)
    #meadow.add_edge(0, 5)
    #meadow.add_edge(0, 6)
    #meadow.add_edge(0, 7)

    #meadow.add_edge(1, 2)
    #meadow.add_edge(1, 3)
    #meadow.add_edge(1, 4)
    return meadow
    
def create_road():
    road=nx.path_graph(4)
    road.add_edge(0, 2)
    return road
    
def create_city():
    city=nx.path_graph(4)
    city.add_edge(0, 2)
    return city