from environment import NetworkEnvironment
from routing import get_shortest_path

def test_shortest_path():
    env = NetworkEnvironment("data/network_topology.json")
    path = get_shortest_path(env.graph, 'A', 'B')
    assert path is not None
