# src/environment.py
import json
import networkx as nx

class NetworkEnvironment:
    def __init__(self, topology_file):
        self.graph = self.load_network_topology(topology_file)

    def load_network_topology(self, topology_file):
        with open(topology_file, 'r') as f:
            data = json.load(f)
        graph = nx.Graph()
        for node in data['nodes']:
            graph.add_node(node['id'], **node)
        for link in data['links']:
            graph.add_edge(link['source'], link['target'], distance=link['distance'])
        return graph

    def get_shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source=source, target=target, weight='distance')
