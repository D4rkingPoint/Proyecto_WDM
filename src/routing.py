# src/routing.py
import networkx as nx

def get_shortest_path(graph, source, target):
    try:
        path = nx.shortest_path(graph, source=source, target=target, weight='distance')
        return path
    except nx.NetworkXNoPath:
        return None
