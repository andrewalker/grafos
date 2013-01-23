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
    pred[s] = None

    Q = [ s ]

    while Q:
        u = Q.pop()
        for v in G[u]:
            if cor[v] == 'branco':
                cor[v] = 'cinza'
                d[v]   = d[u] + 1
                Q.append(v)

            cor[u] = 'preto'

    return ?
