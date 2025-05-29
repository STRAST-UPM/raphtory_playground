# external imports

# internal imports
from src.classes.graphql_server import GraphQLServer
from src.utilities.constants import (
    GRAPHS_DIR
)

# main
if __name__ == '__main__':
    # Start GraphQL server for visualization
    graphql_server = GraphQLServer(GRAPHS_DIR)
    graphql_server.run_server()
