#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

def Prim(G = nx.Graph(), R = None):
    # Q é a lista de vértices que não estão na árvore
    Q    = {}
    # pred armazenará o predecessor de cada vértice
    pred = {}

    # Inicializamos Q com todos os vértices com valor infinito, pois neste
    # ponto ainda não há ligação entre nenhum vértice. Igualmente, nenhum
    # vértice tem predecessor, portanto utilizamos o valor 'null'.
    for v,data in G.nodes(data=True):
        Q[v]    = n.inf
        pred[v] = 'null'

    # Caso não haja pesos definidos para os vértices, atribuímos o valor 1.0.
    # Esta é uma abordagem alternativa à que usamos em Kruskal, de utilizar uma
    # variável para verificar se estamos levando em conta o peso ou não.
    for e,x in G.edges():
        if ('weight' not in G[e][x]):
            G[e][x]['weight'] = 1.0

    # Inicializamos a raiz da árvore com valor 0, e criamos uma árvore chamada
    # MST apenas com os vértices de G.
    Q[R] = 0.0
    MST  = nx.create_empty_copy(G)

    while Q:
        # u := índice do menor elemento de Q
        # pois queremos o vértice de menor peso
        u = min(Q,key=Q.get)

        # removemos de Q, pois ele será adicionado na árvore
        del Q[u]

        # guardamos os pesos mínimos de cada vizinho de u em Q, se forem
        # menores do que os já armazenados
        for vizinho in G[u]:
            if vizinho in Q:
                if G[u][vizinho]['weight'] < Q[vizinho]:
                    pred[vizinho] = u
                    Q[vizinho]    = G[u][vizinho]['weight']

        # Se existirem predecessores para u, então adicionaremos as arestas
        # conectando o vértice u a seus predecessores
        if pred[u] is not 'null':
            for v1,v2,data in G.edges(data=True):
                # para preservar os dados da aresta, foi necessário esse loop
                # que verifica todas as arestas do grafo e procura a aresta
                # (pred(u),u), porém, como um grafo não direcionado da
                # biblioteca não duplica a existência de suas arestas no
                # conjunto de arestas, isto é, se tem (u,v) não tem (v,u), há a
                # necessidade de verificar, no caso de grafos não direcionados,
                # se há a existência da aresta (u,pred(u)) ao invés de
                # (pred(u),u)
                if ( v1 is pred[u] and v2 is u ):
                    MST.add_edge(pred[u],u,data)
                elif (  ( v1 is u and v2 is pred[u] ) and
                        ( not nx.is_directed(G) )  ):
                    MST.add_edge(pred[u],u,data)

    return MST
