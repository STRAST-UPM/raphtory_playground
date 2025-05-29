from os import path

# Directories constants
__PROJECT_DIR = (f"{path.dirname(path.dirname(path.abspath(__file__)))}"
                 .replace("/app/src", ""))

DATASETS = f"{__PROJECT_DIR}/datasets"

# Graphql Server
__GRAPHQL_SERVER_DIR = f"{__PROJECT_DIR}/graphql_server"
GRAPHS_DIR = f"{__GRAPHQL_SERVER_DIR}/graphs"
