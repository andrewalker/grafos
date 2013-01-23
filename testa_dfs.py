#!/usr/bin/env python
# -*- coding: utf-8 -*-

from DFS import DFS
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node('u')
G.add_node('v')
G.add_node('w')
G.add_node('x')
G.add_node('y')
G.add_node('z')

G.add_edge('u', 'v')
G.add_edge('u', 'x')
G.add_edge('x', 'v')
G.add_edge('v', 'y')
G.add_edge('y', 'x')
G.add_edge('w', 'y')
G.add_edge('w', 'z')
G.add_edge('z', 'z')

H = DFS(G, 'u')

# labels = {}
# for v in H.nodes():
#     labels[v] = H.node[v]['begin_time']

# pos = nx.spring_layout(G)
# nx.draw(G, pos)

pos = nx.spring_layout(H)
nx.draw(H, pos)
#nx.draw_networkx_labels(H, pos, labels)
#nx.draw_networkx_edges(H, pos)

plt.show()
