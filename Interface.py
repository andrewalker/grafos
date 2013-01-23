#!/usr/bin/env python

import networkx as nx   #permite manipulação de grafos
from tkinter import *   #Prove interface gráfica para menu
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
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = krl.Kruskal(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_MST_Kruskal.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()

def aplica_prim():
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = pr.Prim(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_MST_Prim.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_largura():
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = bfs.BFS(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_BFS.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_profundidade():
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = dfs.DFS(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_DFS.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_dijkstra():
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = dks.Dijkstra(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_Dijkstra.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_coloracao():
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    G = wp.WelshPowell(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_WelshPowell.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()
    
def aplica_todos():
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    M = krl.Kruskal(G)
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_MST_Kruskal.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    #M = pr.Prim(G)
    #pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_MST_Prim.gexf")
    #nx.write_gexf(G, pathDoArquivoNovo)
    M = bfs.BFS(G)
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_BFS.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    M = dfs.DFS(G)
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_DFS.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    M = dks.Dijkstra(G)
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_Dijkstra.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)
    M = wp.WelshPowell(G)
    pathDoArquivoNovo = pathDoArquivo.replace(".gexf","_WelshPowell.gexf")
    nx.write_gexf(M, pathDoArquivoNovo)

def visualizar():
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
