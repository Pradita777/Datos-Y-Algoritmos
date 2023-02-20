from collections import deque

class GraphAL:
  def __init__(self, size):
    self.size = size
    self.nombreVertice = [""]*size
    self.mapaCiudad = [0]*size
    self.numeroDeVertices = 0
    for i in range(0,size):
      self.mapaCiudad[i] = deque()

  def addArc(self, name1, name2, distancia):
    id1 = self.getId(name1)
    id2 = self.getId(name2)
    fila = self.mapaCiudad[id1]
    parejaDestinoPeso = (id2, distancia)
    fila.append(parejaDestinoPeso)

  def getWeight(self, name1, name2):
    id1 = self.getId(name1)
    id2 = self.getId(name2)
    arreglo = self.mapaCiudad[id1]
    for i in arreglo:
      if i[0] == id2:
        peso = i[1]
    return peso

  def getWeightConId(self, id1, id2):
    peso = 0
    arreglo = self.mapaCiudad[id1]
    for i in arreglo:
      if i[0] == id2:
        peso = i[1]
    return peso

  def getSuccessors(self, vertice):
    lista = []
    arreglo = self.mapaCiudad[vertice]
    for i in arreglo:
      if i[1] != 0:
        lista.append(i[0])
    return lista

  def getId(self, name):
    contador = 0
    for i in self.nombreVertice:
      if i == name:
        return contador
      contador += 1

  def addVertex(self, id, name):
    self.nombreVertice[id] = name
    self.numeroDeVertices += 1

def voraz(grafo,cercano,n,pesoMenor,lista,visitados):
  visitados[getId(cercano)] = 1
  menor = inf
  if cercano == n:
    visitados[getId(cercano)] = 0
    lista.append(cercano)
    return lista,pesoMenor
  else:
    for sucesor in grafo.getSuccessors(cercano):
      peso = grafo.getWeight(getId(cercano),getId(sucesor))
      if peso<menor and not visitados[getId(sucesor)]:
        menor = peso
    pesoMenor+=menor
    lista.append(cercano)
    l,p = backtrack(grafo, sucesor, n,pesoMenor,lista,visitados)
        
  visitados[getId(cercano)] = 0
  return lista,p

def main():
    g = GraphAL(6)
    g.addVertex(1, "Movies")
    g.addVertex(2, "Snell")
    g.addVertex(3, "Hospital")
    g.addVertex(4, "Gym")
    g.addVertex(5, "Planters")
    visitados= [0]*6
    lista = []
    
    g.addArc("Snell", "Gym", 17)
    g.addArc("Gym", "Snell", 4)
    g.addArc("Gym", "Movies", 5)
    g.addArc("Planters", "Movies", 20)
    g.addArc("Movies", "Snell", 12)
    g.addArc("Movies", "Hospital", 7)

    
    print(voraz(g,"Movies", "Gym",0,lista,visitados))

main()