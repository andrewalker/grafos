#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n
import sys

def Dijkstra(G, s):
    Lambda = {}
    Pi = {}
    Q = G.nodes()

    for v in G.nodes():
        Lambda[v] = n.inf

    # Caso não haja pesos definidos para os vértices, atribuímos o valor 1.0.
    # Esta é uma abordagem alternativa à que usamos em Kruskal, de utilizar uma
    # variável para verificar se estamos levando em conta o peso ou não.
    for v1,v2 in G.edges():
        if ('weight' not in G[v1][v2]):
            G[e][x]['weight'] = 1

    Lambda[s] = 0
    Pi[s] = None

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
