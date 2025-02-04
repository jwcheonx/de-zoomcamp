import sys

import polars as pl

print(f"arguments: {sys.argv[1:]}")
print(f"polars version: {pl.__version__}")
