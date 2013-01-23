#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

def Dijkstra(G, s):
    Lambda = {}
    Pi = {}
    Q = G.nodes()

    for v in G.nodes():
        Lambda[v] = n.inf

    Lambda[s] = 0
    Pi[s] = None

    # Não preciso do S devido a checagem de v em Q dentro do IF do FOR

    while Q:
        menor = n.inf
        u     = Q[0]
        if sys.version_info[0] < 3:
            for k,v in Lambda.iteritems():
                if (v < menor) and (k in Q):
                    menor = v
                    u = k
        else:
            for k,v in Lambda.items():
                if (v < menor) and (k in Q):
                    menor = v
                    u = k

        u_index = Q.index(u)
        del Q[u_index]

        for v in G[u]:
            if (v in Q) and (Lambda[v] > Lambda[u] + G[u][v]['weight']):
                Lambda[v] = Lambda[u] + G[u][v]['weight']
                Pi[v] = u

    #retorna a arvore de predecessores com a informação de Lambda[v]

    H = nx.create_empty_copy(G)

    for v1,v2,data in G.edges(data=True):
        if Pi[v2] is v1:
            H.add_edge( v1, v2, data )
            H.node[v1]['lambda'] = Lambda[v1]
            H.node[v2]['lambda'] = Lambda[v2]

    return H
