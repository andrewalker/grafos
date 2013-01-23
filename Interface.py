#!/usr/bin/env python
# -*- coding: utf-8 -*-

import networkx as nx   #permite manipulação de grafos
import sys
if sys.version_info[0] <3:
    from Tkinter import *
    import tkFileDialog as tk
else:
    from tkinter import *   #Prove interface gráfica para menu
    import tkinter.filedialog
import Kruskal as krl
import BFS as bfs
import DFS as dfs
import Dijkstra as dks
import Prim as pr
import WelshPowell as wp
import matplotlib.pyplot as plt
# define options for opening or saving a file
file_opt = options = {}
options['defaultextension'] = '.gexf'
options['initialfile'] = '*.gexf'

def aplica_kruskal():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = krl.Kruskal(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_MST_Kruskal.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()

def aplica_prim():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = pr.Prim(G, G.nodes()[0])
    pathDoArquivo = pathDoArquivo.replace(".gexf","_MST_Prim.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_largura():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = bfs.BFS(G, G.nodes()[0])
    pathDoArquivo = pathDoArquivo.replace(".gexf","_BFS.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_profundidade():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = dfs.DFS(G, G.nodes()[0])
    pathDoArquivo = pathDoArquivo.replace(".gexf","_DFS.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_dijkstra():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = dks.Dijkstra(G, G.nodes()[0])
    pathDoArquivo = pathDoArquivo.replace(".gexf","_Dijkstra.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_coloracao():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = wp.WelshPowell(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_WelshPowell.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_todos():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    M = krl.Kruskal(G)
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_MST_Kruskal.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    M = pr.Prim(G, G.nodes()[0])
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_MST_Prim.gexf")
    nx.write_gexf(G, pathDoArquivoNovo)
    M = bfs.BFS(G, G.nodes()[0])
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_BFS.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    M = dfs.DFS(G, G.nodes()[0])
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_DFS.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    M = dks.Dijkstra(G, G.nodes()[0])
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_Dijkstra.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    M = wp.WelshPowell(G, G.nodes()[0])
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_WelshPowell.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)

def visualizar():
    if sys.version_info[0] <3:
        pathDoArquivo = tk.Open().show()
    else:
        pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    nx.draw(G)
    plt.show()

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.kruskal = Button (self, text="MST-Kruskal", command=aplica_kruskal)
        self.prim = Button(self, text="MST-Prim", command=aplica_prim)
        self.largura = Button(self, text="Busca em Largura", comman=aplica_largura)
        self.profundidade = Button(self, text="Busca em Profundidade", command=aplica_profundidade)
        self.dijkstra = Button(self, text="Caminhos mínimos - Dijkstra", command=aplica_dijkstra)
        self.coloracao = Button(self, text="Coloração de vértices - Welsh & Powell", command=aplica_coloracao)
        self.todos = Button(self, text="Exportar todas as transformações", command=aplica_todos)
        self.visualizar = Button(self, text="Visualizar", command=visualizar)
        self.visualizar.pack()
        self.todos.pack()
        self.coloracao.pack()
        self.dijkstra.pack()
        self.profundidade.pack()
        self.largura.pack()
        self.prim.pack()
        self.kruskal.pack ()
        self.pack()
app = Application()
app.master.title("Algoritmos em Grafos")
app.master.geometry("280x210+190+80")
mainloop()
