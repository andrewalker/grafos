#!/usr/bin/env python
# -*- coding: utf-8 -*-

from BFS import BFS
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('r')
G.add_node('s')
G.add_node('t')
G.add_node('u')
G.add_node('v')
G.add_node('w')
G.add_node('x')
G.add_node('y')

G.add_edge('v', 'r')
G.add_edge('r', 's')
G.add_edge('s', 'w')
G.add_edge('w', 't')
G.add_edge('w', 'x')
G.add_edge('x', 't')
G.add_edge('x', 'u')
G.add_edge('x', 'y')
G.add_edge('t', 'u')
G.add_edge('y', 'u')

H = BFS(G, 's')

labels = {}
for v in H.nodes():
    labels[v] = H.node[v]['depth']

pos = nx.spring_layout(H)
nx.draw(H, pos)
# pos = nx.spring_layout(G)
# nx.draw(G, pos)
#nx.draw_networkx_labels(H, pos, labels)
#nx.draw_networkx_edges(H, pos)

plt.show()
