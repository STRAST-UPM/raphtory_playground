# external imports
from raphtory import Graph

# internal imports
from app.src.classes.helpers.graphql_server import GraphQLServer
from app.src.utilities.constants import (
    GRAPHS_DIR
)
from app.src.utilities.utils import export_graphs_to_file

# main
if __name__ == '__main__':

    # Create a new graph
    graph = Graph()

    # Add some data to your graph
    graph.add_node(timestamp=1, id="Alice")
    graph.add_node(timestamp=1, id="Bob")
    graph.add_node(timestamp=1, id="Charlie")
    graph.add_edge(timestamp=2, src="Bob", dst="Charlie", properties={"weight": 5.0})
    graph.add_edge(timestamp=3, src="Alice", dst="Bob", properties={"weight": 10.0})
    graph.add_edge(timestamp=3, src="Bob", dst="Charlie", properties={"weight": -15.0})

    # Export graphs to GRAPHS_DIR for visualization
    export_graphs_to_file(
        graph_to_export=graph,
        graph_name="test_graph"
    )

    # Start GraphQL server for visualization
    graphql_server = GraphQLServer(GRAPHS_DIR)
    graphql_server.run_server()
