import unittest

from src.Tile import Tile

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


if __name__ == "__main__":
    unittest.main()