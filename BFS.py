#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

def BFS(G, s):
    cor  = {}
    pred = {}
    d    = {}

    for v in G.nodes():
        d[v]    = n.inf
        cor[v]  = 'branco' # branco cinza e preto
        pred[v] = None

    for v1,v2 in G.edges():
        if ('weight' not in G[v1][v2]):
            G[v1][v2]['weight'] = 1

    cor[s]  = 'cinza'
    d[s]    = 0

    Q = [ s ]

    while Q:
        u = Q.pop()
        for v in G[u]:
            if cor[v] == 'branco':
                cor[v]  = 'cinza'
                d[v]    = d[u] + G[u][v]['weight']
                pred[v] = u
                Q.append(v)

            cor[u] = 'preto'

