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

def coloring(G):

    colors = dict()
    colors_list = ['gold', 'red', 'violet', 'pink', 'limegreen',
                   'violet', 'darkorange', 'black', 'white']
    
    nodes_srt = []
    tmp = sorted(G.degree, key=lambda x: x[1], reverse=True)
    for node in tmp:
        nodes_srt.append(node[0])
    
    index = 0
    while len(nodes_srt) > 0 and index < len(colors_list):
        colored_nodes = []
        for node in nodes_srt:
            if len(set(G.neighbors(node)).intersection(set(colored_nodes))) == 0:
                colors[node] = colors_list[index]
                colored_nodes.append(node)
        for node in colored_nodes:
            if node in nodes_srt:
                nodes_srt.remove(node)
        index += 1

        H = G.copy()
        node_colors = []
        for n in H.nodes():
            if n in colors.keys():
                node_colors.append(colors[n])
            else:
                node_colors.append('grey')
        
        graph_name = f"images/random_undirected_{len(G.nodes)}_vx_{len(G.edges)}_{index}.pdf"
        nx.draw(H, node_color=node_colors)
        plt.savefig(graph_name)
        plt.show(graph_name)
        H.clear()

    return colors

G = generate_random_graph(60, 130)
colors = coloring(G)

H = G.copy()
node_colors = []
for n in H.nodes():
    node_colors.append(colors[n])

graph_name = f"images/random_undirected_{len(G.nodes)}_vx_{len(G.edges)}_final.pdf"
nx.draw(H, node_color=node_colors)
plt.savefig(graph_name)
plt.show(graph_name)
