from raphtory import Graph
from datetime import datetime

if __name__ == '__main__':

    g = Graph()
    g.add_node(timestamp="2021-02-03 14:01:15", id=10)

    # Create a python datetime object
    datetime_obj = datetime.fromisoformat("2021-02-03 14:01:30")
    g.add_node(timestamp=datetime_obj, id=10)

    print(g)
    print(g.node(id=10).history())
    print(g.node(id=10).history_date_time())
