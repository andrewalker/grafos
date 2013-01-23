#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

def Dijkstra(G, s, t):
    Lambda = {}
    Pi = {}
    Q = G.nodes()

    for v in G.nodes():
        Lambda[v] = n.inf

    Lambda[s] = 0
    Pi[s] = None

    # Não preciso do S devido a checagem de v em Q dentro do IF do FOR

    while Q:
        u = min(Q) # vertice de menor valor do lambda em Q


        for v in G[u]:
            if (v in Q) and (Lambda[v] > Lambda[u] + G[u][v]['weight']):
                Lambda[v] = Lambda[u] + G[u][v]['weight']
                Pi[v] = u

    #retorna a arvore de predecessores com a informação de Lambda[v]
