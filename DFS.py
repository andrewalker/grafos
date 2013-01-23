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
        cor[v]  = 'branco' # cores possíveis: branco cinza e preto
        pred[v] = None

    for v in G.nodes():
        if cor[v] == 'branco':
            tempo = visit(G, v, cor, pred, d, f, tempo)

    H = nx.create_empty_copy(G)

    for v1,v2,data in G.edges(data=True):
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):
            H.add_edge( v1, v2, data )
            H.node[v1]['begin_time'] = d[v1]
            H.node[v2]['begin_time'] = d[v2]
            H.node[v1]['finish_time'] = f[v1]
            H.node[v2]['finish_time'] = f[v2]

    return H

def visit(G, s, cor, pred, d, f, tempo):
    tempo  = tempo + 1
    d[s]   = tempo
    cor[s] = 'cinza'

    for v in G[s]:
        if cor[v] == 'branco':
            pred[v] = s
            tempo = visit(G, v, cor, pred, d, f, tempo)

    cor[s] = 'preto'
    tempo = tempo + 1
    f[s] = tempo

    return tempo
