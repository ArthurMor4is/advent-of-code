import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "input.txt")

import networkx as nx
import matplotlib.pyplot as plt

def part_1():
    result = None
    G = create_graph()
    cut_edges = nx.minimum_edge_cut(G)
    G.remove_edges_from(cut_edges)
    connected_components = list(nx.connected_components(G))
    return len(connected_components[0]) * len(connected_components[1])

def create_graph():
    G = nx.Graph()
    with open(file_path, "r") as f:
        line = f.readline().replace("\n", "")
        while line:
            # Some logic here
            components = line.split(": ")
            node = components[0]
            neighbors = components[1].split()
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
            line = f.readline()
    return G


if __name__ == "__main__":
    print(part_1())
