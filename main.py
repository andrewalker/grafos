#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx
import tkFileDialog
import MST_Kruskal as mst

file_path = tkFileDialog.askopenfilename()

G = nx.read_gexf(file_path)

print(G.nodes(data=True)[0])
