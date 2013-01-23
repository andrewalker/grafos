#!/usr/bin/env python
# -*- coding: utf-8 -*-
import networkx as nx
import numpy as n

tempo = 0

def DFS(G, s):
    cor  = {}
    pred = {}
    d    = {}
    f    = {}

    for v in G.nodes():
        cor[v]  = 'branco' # branco cinza e preto
        pred[v] = None

    tempo = tempo + 1

    for v in G.nodes():
        if cor[v] == 'branco':
            DFS_VISIT(G,v)

def DFS_VISIT(G, s):
    cor  = {}
    pred = {}
    d    = {}
    f    = {}

    tempo = tempo + 1
    d[s] = tempo
    cor[s] = 'cinza'

    for v in G[s]:
        if cor[v] == 'branco':
            pred[v] = s
            DFS_VISIT(G,v)
    cor[s] = 'preta'
    tempo = tempo + 1
    f[v] = tempo
