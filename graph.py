# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from queue import PriorityQueue
#from colormap import rgb2hex

from edge import Edge
from node import Node


class Graph:
        """
        Clase grafo: Referente al grafo
        """
        def __init__(self,digraph=False,eng = 'fdp'):

                """
                Inicializa un grafo vacío.
                """

                self.id = 'graph'
                self.nodes = dict()
                self.edges = dict()
                self.digraph = digraph
                if digraph:
                        self.display = graphviz.Digraph(format='png',engine=eng)
                else:
                        self.display = graphviz.Graph(format='png',engine = eng)

        def addNode(self, name,pos='0',colour = 'red'):
                """
                Agrega un nodo al grafo con el id name.
                pos: posición del nodo
                """
                if name not in self.nodes.keys():
                        node = Node(name)
                        #colour = rgb2hex(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                        self.nodes[name] = node
                        if pos == '0':
                                self.display.node(name,shape='point',color=colour)
                        else:
                                self.display.node(name,shape='point',color=colour,pos=pos)
                #return self.getNode(name)

        def addEdge(self, name, node0, node1):
                """
                Agrega una arista con nodos node0 y node1 como ids. 
                Crea los nodos si no existen.
                """
                if name not in self.edges.keys():
                        self.addNode(node0)
                        self.addNode(node1)
                        n0 = self.getNode(node0)
                        n1 = self.getNode(node1)
                        e = Edge(n0,n1,name)
                        self.edges[name] = e
                        self.display.edge(node0,node1,color='gray')
                        n0.degree += 1
                        n1.degree += 1
                        n0.neighboors.add(node1)
                        n1.neighboors.add(node0)
                #return e

        def getNode(self,name):
                """
                Invoca al nodo con el id name.
                """
                return self.nodes.get(name)

        def getEdge(self,name):
                """
                Invoca a la arista con el id name.
                """
                return self.edges.get(name)

        def show(self,nombre='graph'):
                """
                Guarda al nodo en el archivo graph.gv para leer en Gephi.
                Guarda una imagen del nodo con el archivo graph.png
                Muestra la imagen.
                """
                self.display.render(filename=nombre+'.gv',view=True)
                im = Image.open(nombre+'.gv.png') #cv2.imread('graph.png')
                im.show()
                #cv2.imshow('img',img) # MODIFICAR 
                #cv2.waitKey()

        def Dijkstra(self,s,posiciones=False):
                """
                Implementa el algoritmo de Dijkstra.
                self: Grafo de entrada.
                s:    id del nodo inicial
                posiciones: Marque True si desea que se coloquen los nodos en las mismas posiciones
                            originales
                            Funciona solamente con grid y geographic.
                """
                G = self
                if posiciones:
                        g = Graph(eng='neato')
                else:
                        g = Graph()
                q = PriorityQueue()
                q2 = PriorityQueue()
                q.put((0,s))
                S = []
                nodos = list(G.nodes.keys())
                D = dict()
                Guardar = dict()
                for n in nodos:
                        D[n] = float('inf')
                D[s] = 0
                distancia_total = 0
                c = 0

                while not q.empty():
                        d,u = q.get()
                        if posiciones:
                                x = G.getNode(u).x
                                y = G.getNode(u).y
                                #print(u,x,y)

                        #print(u in S)

                        if c > 0:
                                if not u in S:
                                        if posiciones:
                                                g.addNode(u + '(' + str(d) + ')',pos=str(x) + ','+ str(y)+'!')
                                        else:
                                                g.addNode(u + '(' + str(d) + ')')
                                d2,u2 = q2.get()
                                d2 = Guardar[u2]
                                if not(u in S and u2 in S):
                                        #print(u2 + '->' + u)
                                        g.addEdge(u2 + '->' + u,u + '(' + str(d) + ')',u2 + '(' + str(d2) + ')')
                        else:
                                if posiciones:
                                        g.addNode(u + '(' + str(d) + ')',pos=str(x) + ','+ str(y)+'!',colour='blue')
                                else:
                                        g.addNode(u + '(' + str(d) + ')',colour='blue')

                        c += 1
                        S.append(u)
                        Vecinos = G.getNode(u).neighboors

                        for v in Vecinos:
                                edge = G.edges.get(u + '->' + v)
                                if edge:
                                        d2 = edge.distance
                                else:
                                        edge = G.edges.get(v + '->' + u)
                                        d2 = edge.distance

                                if v not in S:
                                        dv = D[v]
                                        du = D[u]
                                        if dv > du + d2:
                                                dv = du + d2
                                                distancia_total += dv
                                                q.put((dv,v))
                                                q2.put((dv,u))
                                                Guardar[u] = d
                                                D[v] = dv

                return g

