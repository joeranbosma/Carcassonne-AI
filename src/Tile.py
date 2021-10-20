"""
Object representing Tile

"""


class Tile:
    def __init__(self, meadow=None, road=None, town=None):
        self.meadow = meadow
        self.road = road
        self.town = town

    def add_two(self, x):
        return x + 2

    #   meadow = nx.path_graph(8)
    #   road = nx.path_graph(4)
    #   town = nx.path_graph(4)

    def meadow_is_connected():
        pass
