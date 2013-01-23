#!/usr/bin/env python

import networkx as nx   #permite manipulação de grafos
from tkinter import *   #Prove interface gráfica para menu
import MST_Kruskal as krl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
# define options for opening or saving a file
file_opt = options = {}
options['defaultextension'] = '.gexf'
options['initialfile'] = '*.gexf'

def abrir(G):
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    nx.draw(G, hold=None)
    plt.show()
    global arquivoLido
def exportar(G):
    pathDoArquivoSalvar = filedialog.asksaveasfilename(**file_opt)
    print(pathDoArquivoSalvar)
    #nx.write_gexf(G, pathDoArquivoSalvar)
    nx.draw(G)
    plt.show()
def ajuda() : print ("ajuda")

def aplica_kruskal():
    pathDoArquivo = filedialog.askopenfilename()
    G = nx.read_gexf(pathDoArquivo)
    nx.draw(G)
    plt.show()
    G = krl.MST_Kruskal(G)
    pathDoArquivo = pathDoArquivo.replace(".gexf","_MST_Kruskal.gexf")
    nx.write_gexf(G, pathDoArquivo)
    nx.draw(G)
    plt.show()

def aplica_prim():
    pass
def aplica_largura():
    pass
def aplica_profundidade():
    pass
def aplica_djikstra():
    pass
def aplica_coloracao():
    pass
def aplica_todos():
    pass

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.kruskal = Button (self, text="MST-Kruskal", command=aplica_kruskal)
        self.prim = Button(self, text="MST-Prim", command=aplica_prim)
        self.largura = Button(self, text="Busca em Largura", comman=aplica_largura)
        self.profundidade = Button(self, text="Busca em Profundidade", command=aplica_profundidade)
        self.djikstra = Button(self, text="Caminhos mínimos - Djikstra", command=aplica_djikstra)
        self.coloracao = Button(self, text="Coloração de vértices - Welsh & Powell", command=aplica_coloracao)
        self.todos = Button(self, text="Exportar todas as transformações", command=aplica_todos)
        self.todos.pack()
        self.coloracao.pack()
        self.djikstra.pack()
        self.profundidade.pack()
        self.largura.pack()
        self.prim.pack()
        self.kruskal.pack ()
        self.pack()
app = Application()
app.master.title("Algoritmos em Grafos")
app.master.geometry("280x180+180+80")
mainloop()
