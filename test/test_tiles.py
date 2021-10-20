import unittest
import networkx as nx
from src.Tile import Tile
from src.create_tiles import create_meadow

class TestMain(unittest.TestCase):
    """ """

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tile=Tile()

    def test_add_two(self):
        result = self.tile.add_two(3)
        expected_result=5
        self.assertEqual(expected_result, result)
    
    def test_road_connected(self):
        meadow=create_meadow()
        self.assertTrue(meadow.has_edge(0, 5))

if __name__ == "__main__":
    unittest.main()