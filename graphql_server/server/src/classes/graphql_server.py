# external imports

# internal imports
from raphtory import graphql

class GraphQLServer:

    def __init__(self, working_dir: str):
        self._working_dir = working_dir

        self._server_instance = graphql.GraphServer(working_dir)

    @property
    def server_instance(self):
        return self._server_instance

    @property
    def working_dir(self):
        return self._working_dir

    def run_server(self):
        self._server_instance.run()
