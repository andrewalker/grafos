#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

def DFS(G, s):
    cor  = {}
    pred = {}
    d    = {}
    f    = {}

    tempo = 0

    for v in G.nodes():
        cor[v]  = 'branco' # branco cinza e preto
        pred[v] = None

    for v in G.nodes():
        if cor[v] == 'branco':
            tempo = visit(G, v, cor, pred, d, f, tempo)

    H = nx.create_empty_copy(G)

    for v1,v2,data in G.edges(data=True):
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):
            H.add_edge( v1, v2, data )

    return H

def visit(G, s, cor, pred, d, f, tempo):
    tempo  = tempo + 1
    d[s]   = tempo
    cor[s] = 'cinza'

    for v in G[s]:
        if cor[v] == 'branco':
            pred[v] = s
            visit(G, v, cor, pred, d, f, tempo)

    cor[s] = 'preto'
    tempo = tempo + 1
    f[s] = tempo

    return tempo
