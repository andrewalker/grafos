#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx

# Função auxiliar para encontrar o índice do conjunto em que o vértice se
# encontra
def encontrar_conjunto(lista, vertice):
    i = 0
    for conjunto in lista:
        if (vertice in conjunto):
            return i
        i = i+1

def Kruskal(G):
    if 'weight' in G.edges(data=True)[0][2]:
        grafo_com_peso = True
    else:
        grafo_com_peso = False

    MST = nx.create_empty_copy(G)

    if grafo_com_peso:
        E = sorted(G.edges(data=True), key=lambda k: k[2]['weight'])
    else:
        E = G.edges(data=True)

    vertices_conexos = []

    # criamos uma lista de conjuntos disjuntos com apenas um vértice cada um, a
    # princípio, para depois fazermos as uniões
    for v in G.nodes():
        vertices_conexos.append({v})

    for aresta in E:
        indexConj1 = encontrar_conjunto(vertices_conexos, aresta[0])
        indexConj2 = encontrar_conjunto(vertices_conexos, aresta[1])

        # Se o conjunto encontrado para o vértice 0 é o mesmo do vértice 1,
        # então não podemos uni-los, já que isto fecharia um ciclo.
        if indexConj1 != indexConj2:

            # Se o grafo contém o peso, então adicionamos as três informações
            # da aresta (2 vértices e dados)
            if grafo_com_peso:
                MST.add_edge(aresta[0], aresta[1], aresta[2])
            else:
                MST.add_edge(aresta[0], aresta[1])

            # removemos os dois conjuntos de vértices do vetor vertices_conexos
            if indexConj1 > indexConj2:
                conj1 = vertices_conexos.pop(indexConj1)
                conj2 = vertices_conexos.pop(indexConj2)
            else:
                conj2 = vertices_conexos.pop(indexConj2)
                conj1 = vertices_conexos.pop(indexConj1)

            # e inserimos um novo conjunto a partir da união dos dois
            vertices_conexos.append(conj1.union(conj2))

    return MST
