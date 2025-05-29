# external imports
from os import path

# Directories constants
__PROJECT_DIR = (f"{path.dirname(path.dirname(path.abspath(__file__)))}"
              .replace("/server/src", ""))

GRAPHS_DIR = f"{__PROJECT_DIR}/graphs"
