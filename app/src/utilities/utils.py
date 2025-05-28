# external imports
import os
from raphtory.raphtory import Graph

# internal imports
from app.src.utilities.constants import (
    GRAPHS_DIR
)

# Utils functions
def export_graphs_to_file(graph_to_export: Graph, graph_name: str) -> None:
    """
    This function exports graphs to a file inside the GRAPHS_DIR. It overwrites
    the previously exported graph with the same name.

    :param graph_to_export:
    :param graph_name:
    :return: None
    """
    graph_path = os.path.join(GRAPHS_DIR, graph_name)
    if not os.path.exists(GRAPHS_DIR):
        os.makedirs(GRAPHS_DIR)
    if os.path.exists(graph_path):
        os.remove(graph_path)
    graph_to_export.save_to_file(graph_path)
