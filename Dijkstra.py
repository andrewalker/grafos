#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

def Dijkstra(G, s, t):
    S = {}
    Q = G.nodes()

    for v in G.nodes():
        S[v] = n.inf

    S[s] = 0

    backtrack = {}

    for v in G.nodes():
        backtrack[v] = []

    while Q:
        u = min(Q)

        if u is t:
            break

        u_index = Q.index(u)
        del Q[u_index]

        for v in G[u]:
            if (v in Q) and (S[v] > S[u] + G[u][v]['weight']):
                S[v] = S[u] + G[u][v]['weight']
                backtrack[v].append(u)

    vertices_subgrafo = [ t ]
    b = backtrack[t].pop()

    while b:
        vertices_subgrafo.append(b)
        v = b
        if backtrack[v]:
            b = backtrack[v].pop()
        else:
            b = 0

    vertices_subgrafo.reverse()
    caminho = []

    for i in range(len(vertices_subgrafo)-1):
        caminho.append([ vertices_subgrafo[i], vertices_subgrafo[i+1] ])

    P = G.subgraph(vertices_subgrafo)

    for aresta in P.edges():
        if aresta not in caminho:
            P.remove_edge(*aresta)

    return P
