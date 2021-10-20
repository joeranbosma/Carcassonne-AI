import unittest
import networkx as nx
from src.Tile import Tile
from src.create_tiles import create_meadow
from src.create_tiles import create_road
from src.create_tiles import create_town


class TestMain(unittest.TestCase):
    """ """

    # Initialize test object
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tile = Tile()

    def test_add_two(self):
        result = self.tile.add_two(3)
        expected_result = 5
        self.assertEqual(expected_result, result)

    def test_example_meadow(self):
        meadow = create_meadow()
        expected_nr_of_nodes = 8
        expected_nr_of_edges = 12
        self.assertEqual(meadow.number_of_nodes(), expected_nr_of_nodes)
        self.assertEqual(meadow.number_of_edges(), expected_nr_of_edges)

        self.assertFalse(meadow.has_edge(0, 0))
        self.assertFalse(meadow.has_edge(0, 1))
        self.assertFalse(meadow.has_edge(0, 2))
        self.assertFalse(meadow.has_edge(0, 3))
        self.assertFalse(meadow.has_edge(0, 4))
        self.assertTrue(meadow.has_edge(0, 5))
        self.assertTrue(meadow.has_edge(0, 6))
        self.assertTrue(meadow.has_edge(0, 7))

        self.assertFalse(meadow.has_edge(1, 0))
        self.assertFalse(meadow.has_edge(1, 1))
        self.assertTrue(meadow.has_edge(1, 2))
        self.assertTrue(meadow.has_edge(1, 3))
        self.assertTrue(meadow.has_edge(1, 4))
        self.assertFalse(meadow.has_edge(1, 5))
        self.assertFalse(meadow.has_edge(1, 6))
        self.assertFalse(meadow.has_edge(1, 7))

        self.assertFalse(meadow.has_edge(2, 0))
        self.assertTrue(meadow.has_edge(2, 1))
        self.assertFalse(meadow.has_edge(2, 2))
        self.assertTrue(meadow.has_edge(2, 3))
        self.assertTrue(meadow.has_edge(2, 4))
        self.assertFalse(meadow.has_edge(2, 5))
        self.assertFalse(meadow.has_edge(2, 6))
        self.assertFalse(meadow.has_edge(2, 7))

        self.assertFalse(meadow.has_edge(3, 0))
        self.assertTrue(meadow.has_edge(3, 1))
        self.assertTrue(meadow.has_edge(3, 2))
        self.assertFalse(meadow.has_edge(3, 3))
        self.assertTrue(meadow.has_edge(3, 4))
        self.assertFalse(meadow.has_edge(3, 5))
        self.assertFalse(meadow.has_edge(3, 6))
        self.assertFalse(meadow.has_edge(3, 7))

        self.assertFalse(meadow.has_edge(4, 0))
        self.assertTrue(meadow.has_edge(4, 1))
        self.assertTrue(meadow.has_edge(4, 2))
        self.assertTrue(meadow.has_edge(4, 3))
        self.assertFalse(meadow.has_edge(4, 4))
        self.assertFalse(meadow.has_edge(4, 5))
        self.assertFalse(meadow.has_edge(4, 6))
        self.assertFalse(meadow.has_edge(4, 7))

        self.assertTrue(meadow.has_edge(5, 0))
        self.assertFalse(meadow.has_edge(5, 1))
        self.assertFalse(meadow.has_edge(5, 2))
        self.assertFalse(meadow.has_edge(5, 3))
        self.assertFalse(meadow.has_edge(5, 4))
        self.assertFalse(meadow.has_edge(5, 5))
        self.assertTrue(meadow.has_edge(5, 6))
        self.assertTrue(meadow.has_edge(5, 7))

        self.assertTrue(meadow.has_edge(6, 0))
        self.assertFalse(meadow.has_edge(6, 1))
        self.assertFalse(meadow.has_edge(6, 2))
        self.assertFalse(meadow.has_edge(6, 3))
        self.assertFalse(meadow.has_edge(6, 4))
        self.assertTrue(meadow.has_edge(6, 5))
        self.assertFalse(meadow.has_edge(6, 6))
        self.assertTrue(meadow.has_edge(6, 7))

        self.assertTrue(meadow.has_edge(7, 0))
        self.assertFalse(meadow.has_edge(7, 1))
        self.assertFalse(meadow.has_edge(7, 2))
        self.assertFalse(meadow.has_edge(7, 3))
        self.assertFalse(meadow.has_edge(7, 4))
        self.assertTrue(meadow.has_edge(7, 5))
        self.assertTrue(meadow.has_edge(7, 6))
        self.assertFalse(meadow.has_edge(7, 7))

    def test_example_road(self):
        road = create_road()
        expected_nr_of_nodes = 4
        expected_nr_of_edges = 1
        self.assertEqual(road.number_of_nodes(), expected_nr_of_nodes)
        self.assertEqual(road.number_of_edges(), expected_nr_of_edges)

        self.assertFalse(road.has_edge(0, 0))
        self.assertFalse(road.has_edge(0, 1))
        self.assertTrue(road.has_edge(0, 2))
        self.assertFalse(road.has_edge(0, 3))

        self.assertFalse(road.has_edge(1, 0))
        self.assertFalse(road.has_edge(1, 1))
        self.assertFalse(road.has_edge(1, 2))
        self.assertFalse(road.has_edge(1, 3))

        self.assertTrue(road.has_edge(2, 0))
        self.assertFalse(road.has_edge(2, 1))
        self.assertFalse(road.has_edge(2, 2))
        self.assertFalse(road.has_edge(2, 3))

        self.assertFalse(road.has_edge(3, 0))
        self.assertFalse(road.has_edge(3, 1))
        self.assertFalse(road.has_edge(3, 2))
        self.assertFalse(road.has_edge(3, 3))


if __name__ == "__main__":
    unittest.main()
