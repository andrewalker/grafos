#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx

def find_set(lista, vertice):
    i = 0
    for conj in lista:
        if (vertice in conj):
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
    for v in G.nodes():
        vertices_conexos.append({v})    #cria uma lista de conjuntos
    for edge in E:
        indexConj1 = find_set(vertices_conexos, edge[0])
        indexConj2 = find_set(vertices_conexos, edge[1])
        if indexConj1 != indexConj2:
            if grafo_com_peso:
                MST.add_edge(edge[0],edge[1],edge[2]) #adiciona as três informações da aresta (2 vértices e dados)
            else:
                MST.add_edge(edge[0],edge[1])
            if indexConj1>indexConj2 :
                conj1 = vertices_conexos.pop(indexConj1)
                conj2 = vertices_conexos.pop(indexConj2)
            else:
                conj2 = vertices_conexos.pop(indexConj2)
                conj1 = vertices_conexos.pop(indexConj1)
            vertices_conexos.append(conj1.union(conj2))
    return MST
