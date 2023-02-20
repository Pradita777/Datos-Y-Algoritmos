import pandas as pd
from collections import deque
from cmath import inf
import sys
class GraphAL:
  def __init__(self, vertx):
    self.V = vertx
    self.numero = {}
    self.añadido = {}
    self.graph = [[0 for column in range(vertx)]for row in range(vertx)]
    self.acoso = [[0 for column in range(vertx)]for row in range(vertx)]
    self.calles = [["" for column in range(vertx)]for row in range(vertx)]
    self.contador = 0

  def addArc(self, name, vertex, destino, weight, oneWay, acoso):
    if vertex not in self.ArregloDeListas and destino in self.ArregloDeListas and oneWay == True:
      self.numero[vertex] = self.contador
      self.calles[self.contador][self.getContador(destino)] = name
      self.graph[self.contador][self.getContador(destino)] = weight
      self.acoso[self.contador][self.getContador(destino)] = acoso
      self.ArregloDeListas.append(vertex)
      self.contador += 1
    if vertex not in self.ArregloDeListas and destino in self.ArregloDeListas and oneWay == False:
      self.numero[vertex] = self.contador
      self.calles[self.contador][self.getContador(destino)] = name
      self.calles[self.getContador(destino)][self.contador] = name
      self.graph[self.contador][self.getContador(destino)] = weight
      self.graph[self.getContador(destino)][self.contador] = weight
      self.acoso[self.contador][self.getContador(destino)] = acoso
      self.acoso[self.getContador(destino)][self.contador] = acoso
      self.ArregloDeListas.append(vertex)
      self.contador += 1
    if vertex in self.ArregloDeListas and destino not in self.ArregloDeListas and oneWay == True:
      self.numero[destino] = self.contador
      self.calles[self.getContador(vertex)][self.contador] = name
      self.graph[self.getContador(vertex)][self.contador] = weight
      self.acoso[self.getContador(vertex)][self.contador] = acoso
      self.ArregloDeListas.append(destino)
      self.contador += 1
    if vertex in self.ArregloDeListas and destino not in self.ArregloDeListas and oneWay == False:
      self.numero[destino] = self.contador
      self.calles[self.contador][self.getContador(vertex)] = name
      self.calles[self.getContador(vertex)][self.contador] = name
      self.graph[self.contador][self.getContador(vertex)] = weight
      self.graph[self.getContador(vertex)][self.contador] = weight
      self.acoso[self.contador][self.getContador(vertex)] = acoso
      self.acoso[self.getContador(vertex)][self.contador] = acoso
      self.ArregloDeListas.append(destino)
      self.contador += 1
    if vertex not in self.ArregloDeListas and destino not in self.ArregloDeListas and oneWay == True:
      self.numero[vertex] = self.contador
      self.numero[destino] = self.contador+1
      self.calles[self.contador][self.contador+1] = name
      self.acoso[self.contador][self.contador+1] = acoso
      self.graph[self.contador][self.contador+1] = weight
      self.ArregloDeListas.append(vertex)
      self.ArregloDeListas.append(destino)
      self.contador += 2
    if vertex not in self.ArregloDeListas and destino not in self.ArregloDeListas and oneWay == False:
      self.numero[vertex] = self.contador
      self.numero[destino] = self.contador+1
      self.calles[self.contador][self.contador+1] = name
      self.calles[self.contador+1][self.contador] = name
      self.acoso[self.contador][self.contador+1] = acoso
      self.acoso[self.contador+1][self.contador] = acoso
      self.graph[self.contador][self.contador+1] = weight
      self.graph[self.contador+1][self.contador] = weight
      self.ArregloDeListas.append(vertex)
      self.ArregloDeListas.append(destino)
      self.contador += 2
      
  def getWeight(self, vertex, destination):
    return self.graph[vertex][destination]

  def getContador(self,vertex):
    return self.contador[vertex]

  def pSol(self, dist,aco):
    print("Distance of vertex from destino")
    for node in range(self.V):
      print(node, "t", dist[node])
      print(node,"t",aco[node])
          
  def minDistance(self, dist, sptSet, aco):
    min = inf 
    for v in range(self.V):
      if dist[v] < min and sptSet[v] == False:
        min = dist[v]
        min_index = v
    return min_index,
    
  def dijk(self, source, ponderado):
    dist = [sys.maxsize] * self.V
    aco = [sys.maxsize] * self.V
    dist[source] = 0
    aco[source] = 0
    sptSet = [False] * self.V
    for cout in range(self.V):
      u = self.minDistance(dist, sptSet)
      sptSet[u] = True
      for v in range(self.V):
        if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v] and self.acoso[u][v]<ponderado:
          aco[v] = aco[u] + self.acoso[u][v]
          dist[v] = dist[u] + self.graph[u][v]
    self.pSol(dist,aco)  

    
def main():
  count = 0
  df = pd.read_csv("calles_de_medellin_con_acoso.csv", delimiter=";")
  lista = df.to_numpy().tolist()
  for i in lista:
    count+= 1
  g = GraphAL(count)
  for i in lista:
    g.addArc(i[0], i[1], i[2], i[3], i[4], i[5])
  g.djikstra("(-75.5715105, 6.2063061)", "(-75.5685931, 6.2073652)",120)
        
main()