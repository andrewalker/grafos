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
        cor[v]  = 'branco' # branco cinza e preto
        pred[v] = None

    tempo = tempo + 1

    for v in G.nodes():
        if cor[v] == 'branco':
            tempo = visit(G, v, cor, pred, d, f, tempo)

def visit(G, s, cor, pred, d, f, tempo):
    tempo  = tempo + 1
    d[s]   = tempo
    cor[s] = 'cinza'

    for v in G[s]:
        if cor[v] == 'branco':
            pred[v] = s
            visit(G,v, cor, pred, d, f)

    cor[s] = 'preta'
    tempo = tempo + 1
    f[v] = tempo

    return tempo
