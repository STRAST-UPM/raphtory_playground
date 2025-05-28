from os import path

# Directories constants
__BASE_DIR = (f"{path.dirname(path.dirname(path.abspath(__file__)))}"
              .replace("/app/src", ""))

GRAPHS_DIR = f"{__BASE_DIR}/graphs"
DATASETS = f"{__BASE_DIR}/datasets"
