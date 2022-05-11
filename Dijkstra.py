from graph import Graph
from erdosRenyi import randomErdosRenyi
from gilbert import randomGilbert
from geographic import randomGeographic
from barabasiAlbert import randomBarabasiAlbert
from grid import grid
from dorogovtsevMendes import dorogovtsevMendes
from queue import PriorityQueue

"""
def Dijkstra(G,s): # No olvidar insertarlo en la clase grafo
        g = Graph(eng='neato')
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
        #print('D')
        c = 0
        while not q.empty():
                d,u = q.get()
                x = G.getNode(u).x 
                y = G.getNode(u).y 
                #g.addNode(u)
                
                if c > 0:
                        g.addNode(u + '(' + str(d) + ')',pos=str(x) + ','+ str(y)+'!')
                        #print(u + '(' + str(d) + ')')
                        d2,u2 = q2.get()
                        d2 = Guardar[u2]
                        #print(u in S,u2 in S)
                        if not(u in S and u2 in S):
                                #print("Edge")
                                #print(u + '(' + str(d) + ')')
                                #print(u2 + '(' + str(d2) + ')')
                                g.addEdge(u2 + '->' + u,u + '(' + str(d) + ')',u2 + '(' + str(d2) + ')')
                else:
                        #print(u + '(' + str(d) + ')')
                        g.addNode(u + '(' + str(d) + ')',pos=str(x) + ','+ str(y)+'!',colour='blue')
                c += 1
                S.append(u)
                Vecinos = G.getNode(u).neighboors
                #print('C')
                for v in Vecinos:
                        #print('B')
                        edge = G.edges.get(u + '->' + v)
                        if edge:
                                d2 = edge.distance
                        else: 
                                edge = G.edges.get(v + '->' + u)
                                d2 = edge.distance
                        if v not in S:
                                dv = D[v]
                                du = D[u]
                                #print('A')
                                if dv > du + d2:
                                        dv = du + d2 
                                        distancia_total += dv
                                        q.put((dv,v))
                                        q2.put((dv,u))
                                        Guardar[u] = d
                                        D[v] = dv
        #print(distancia_total)
        return g
"""

#g1 = randomErdosRenyi(500,700)
#g1.show(nombre='erdosRenyi500_700')

#g1 = randomGilbert(500,0.1)
#g1.show(nombre='gilbert500_01')

#g1 = randomGeographic(20,1.6)
#g1.show(nombre='geographic_20_1_6')

g1 = randomBarabasiAlbert(30,3)
g1.show(nombre='barabasiAlbert_30_3')

#g1 = grid(50,10)
#g1.show(nombre='grid50_10')

#g1 = dorogovtsevMendes(500)
#g1.show(nombre='dorogovtsevMendes500')

#g2 = DFS_I(g1,'1')
g2 = g1.Dijkstra('1')#,posiciones=True)
g2.show(nombre='Dijkstra_barabasiAlbert_30_3')
