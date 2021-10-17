# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import random

def generate_random_graph(n_nodes, n_edges):
    G = nx.Graph()

    if n_edges > n_nodes * (n_nodes - 1) / 2:
        raise NotImplementedError

    all_edges = [{i, j} for i in range(1, n_nodes + 1) for j in range(i + 1, n_nodes + 1)]
    all_edges = [edge for edge in all_edges if len(edge) == 2]
    random.shuffle(all_edges)

    for i in range(1, n_nodes + 1):
        G.add_node(i)

    for j in range(n_edges):
        random_edge = all_edges.pop()
        node_a = random_edge.pop()
        node_b = random_edge.pop()
        G.add_edge(node_a, node_b)
          
    return G

def line_graph(G):
    
    LG = nx.Graph()

    edges = []
    for index, edge in enumerate(G.edges):
        LG.add_node(edge)

    for index, node in enumerate(LG.nodes):
        for index_2, node_2 in enumerate(LG.nodes):
            if node != node_2 and (node[0] in node_2 or node[1] in node_2):
                if (node_2, node) not in LG.edges:
                    LG.add_edge(node, node_2)
    return LG

G = generate_random_graph(60, 130)

graph_name = f"images/random_graph_{len(G.nodes)}_vx_{len(G.edges)}_final.pdf"
nx.draw(G)
plt.savefig(graph_name)
plt.show(graph_name)

LG = line_graph(G)

graph_name = f"images/line_graph_{len(G.nodes)}_vx_{len(G.edges)}_final.pdf"
nx.draw(LG)
plt.savefig(graph_name)
plt.show(graph_name)

check = 0
for node, degree in G.degree:
    check = check + (degree ** 2)
check = check / 2
check = check - len(G.edges)
if check == len(LG.edges):
    print('Correct line graph.')
else:
    print('Incorrect line graph.')