#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n
import sys

def Dijkstra(G, s):
    Lambda = {}             # valores de "peso" para cada vértice
    pred = {}               # predecessores
    Q = G.nodes()           # vértices que ainda não estão na árvore de
                            # caminhos mínimos

    # inicializamos todos os lambdas com infinito
    for v in G.nodes():
        Lambda[v] = n.inf

    # Caso não haja pesos definidos para os vértices, atribuímos o valor 1
    for v1,v2 in G.edges():
        if ('weight' not in G[v1][v2]):
            G[v1][v2]['weight'] = 1

    Lambda[s] = 0
    pred[s] = None

    while Q:

        # encontramos o menor valor de Lambda pertencente a Q
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

        # removemos o item de Q, já que está sendo inserido na árvore
        u_index = Q.index(u)
        del Q[u_index]

        # percorremos a vizinhança de u procurando pesos menores
        for v in G[u]:
            if (v in Q) and (Lambda[v] > Lambda[u] + G[u][v]['weight']):
                Lambda[v] = Lambda[u] + G[u][v]['weight']
                pred[v] = u

    # Criamos um novo grafo vazio do mesmo tipo de G
    H = nx.create_empty_copy(G)

    # Adicionamos os vértices de acordo com os dados de G
    for v1,v2,data in G.edges(data=True):
        if (pred[v2] is v1) or (pred[v1] is v2 and not nx.is_directed(H)):
            H.add_edge( v1, v2, data )
            H.node[v1]['lambda'] = Lambda[v1]
            H.node[v2]['lambda'] = Lambda[v2]

    # Retornamos a árvore de predecessores com a informação de Lambda[v]
    return H
