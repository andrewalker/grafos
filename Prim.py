import networkx as nx
import numpy as n

def Prim(G = nx.Graph(), R = None):
    Q    = {}
    pred = {}

    for v,data in G.nodes(data=True):
        Q[v] = n.inf
        pred[v] = 'null'

    for e,x in G.edges():
        if('weight' not in G[e][x]):
            G[e][x]['weight'] = 1.0

    Q[R] = 0.0
    MST = nx.create_empty_copy(G)

    while Q:
        U = min(Q,key=Q.get)
        del Q[U]

        for vizinho in G[U]:
            if vizinho in Q:
                if G[U][vizinho]['weight'] < Q[vizinho]:
                    pred[vizinho] = U
                    Q[vizinho] = G[U][vizinho]['weight']

        if pred[U] is not 'null':
            for e,x,data in G.edges(data=True):
                if((e is pred[U])and (x is U)):
                    MST.add_edge(pred[U],U,data)
                elif(((e is U)and (x is pred[U])) and(not nx.is_directed(G))):
                    MST.add_edge(pred[U],U,data)

    return MST
