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

    cor[s]  = 'cinza'
    d[s]    = 0

    Q = [ s ]

    while Q:
        u = Q.pop()
        for v in G[u]:
            if cor[v] == 'branco':
                cor[v]  = 'cinza'
                d[v]    = d[u] + 1
                pred[v] = u
                Q.append(v)

            cor[u] = 'preto'

    H = nx.create_empty_copy(G)

    for v2,v1 in pred.interitems():
        if not H.has_node(v1):
            H.add_node(v1)
        if not H.has_node(v2):
            H.add_node(v2)

        e = G[v1][v2]
        H.add_edge(*e)

    return H
