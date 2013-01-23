#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Kruskal as k
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('e')
G.add_node('f')
G.add_node('g')
G.add_node('h')
G.add_node('i')

G.add_edge('a', 'b', weight=4)
G.add_edge('a', 'h', weight=8)
G.add_edge('b', 'h', weight=11)
G.add_edge('b', 'c', weight=8)
G.add_edge('c', 'i', weight=2)
G.add_edge('c', 'f', weight=4)
G.add_edge('c', 'd', weight=7)
G.add_edge('d', 'f', weight=14)
G.add_edge('d', 'e', weight=9)
G.add_edge('e', 'f', weight=10)
G.add_edge('i', 'g', weight=6)
G.add_edge('g', 'h', weight=1)
G.add_edge('h', 'i', weight=7)
G.add_edge('g', 'f', weight=2)

H = k.Kruskal(G)

nx.draw(H)
plt.show()
