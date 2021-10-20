"""
Runs the main code.

"""
import argparse

from src.create_tiles import create_meadow

# from code.test.helper import create_manual_test_graph
import networkx as nx
import pickle

# Read command line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--k", type=int, nargs="?", help="Provide constant k for algorithm 2"
)
parser.add_argument("infile", nargs="?", type=argparse.FileType("r"))

# Set default argument values and parse input arguments
parser.set_defaults(k=10,)
args = parser.parse_args()

# Run main code
print(f"Hello world")
meadow = create_meadow()
print(f"Done.")

# Do something
if args.infile:
    args.infile.close()
