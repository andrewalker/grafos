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
        # U := índice do menor elemento de Q
        # pois queremos o vértice de menor peso
        U = min(Q,key=Q.get)

        # removemos de Q, pois ele será adicionado na árvore
        del Q[U]

        # guardamos os pesos mínimos de cada vizinho de U em Q, se forem
        # menores do que os já armazenados
        for vizinho in G[U]:
            if vizinho in Q:
                if G[U][vizinho]['weight'] < Q[vizinho]:
                    pred[vizinho] = U
                    Q[vizinho]    = G[U][vizinho]['weight']

        if pred[U] is not 'null':
            for v1,v2,data in G.edges(data=True):
                if ( (v1 is pred[U]) and (v2 is U) ):
                    MST.add_edge(pred[U],U,data)
                elif (  ( (v1 is U) and (v2 is pred[U]) ) and ( not nx.is_directed(G) )  ):
                    MST.add_edge(pred[U],U,data)

    return MST
