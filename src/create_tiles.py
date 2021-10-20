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
    meadow=nx.path_graph(8)
    meadow.add_edge(0, 5)
    meadow.add_edge(0, 6)
    meadow.add_edge(0, 7)
    
    meadow.add_edge(1, 2)
    meadow.add_edge(1, 3)
    meadow.add_edge(1, 4)
    return meadow
    
    #road=nx.path_graph(4)
    #city=nx.path_graph(4)