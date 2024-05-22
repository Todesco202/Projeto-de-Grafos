"Caio Eduardo Todesco Gomes RA: 10358993"
import os

class GrafoMatND:
  TAM_MAX_DEFAULT = 180
  inf = float('inf')
  
  def __init__(self, n=TAM_MAX_DEFAULT, rotulado = False):
    self.n = n  
    self.m = 0  
    self.rotulado = rotulado
    self.grafo = [[self.inf for i in range(n)] for j in range(n)]
    self.vertices=[]
    
  def insereVerticeInicial(self, vertice):
    #print(self.vertices)
    self.vertices = vertice
    
  def insereVertice(self, vertice):
    self.vertices.append(vertice)
    self.n += 1
    nova_linha = [self.inf] * self.n
    for linha in self.grafo:
      linha.append(self.inf)
    self.grafo.append(nova_linha)
    print("\nO local e a estação foram inseridos")
    
  def indiceNome(self, local):
    for i in range(len(self.vertices)):
      if self.vertices[i].local == local:
        return i
    return -1
        
  def insereA(self, v, w, rotulo = inf):
    posicao_v = self.indiceNome(v)
    posicao_w = self.indiceNome(w)
    if posicao_v != -1 and posicao_w != -1:
      if self.grafo[posicao_v][posicao_w] == self.inf:
        self.grafo[posicao_v][posicao_w] = rotulo
        self.grafo[posicao_w][posicao_v] = rotulo
        self.m+=1
      else:
        self.grafo[posicao_v][posicao_w] = rotulo
        self.grafo[posicao_w][posicao_v] = rotulo
    else:
      print("\n>>>Um dos locais inseridos é inexistente")

  def removerVertice(self, vertice):
    contem = False
    for i in self.vertices:
      if vertice in i.local:
        contem = True
    if contem:
      verticeIndex = self.indiceNome(vertice)
      for i in range(self.n):
        vertice_dest = self.vertices[i].local
        self.removeA(vertice,vertice_dest)
      self.grafo.pop(verticeIndex)
      self.n -= 1 
      for i in self.grafo:        
        i.pop(verticeIndex)
      self.vertices.pop(verticeIndex)
    else:
      print("Local não está na lista")

 
  def removeA(self, v, w):
    posicao_v = self.indiceNome(v)
    posicao_w = self.indiceNome(w)
    if posicao_v != -1 and posicao_w != -1:
      if self.grafo[posicao_v][posicao_w] != self.inf and self.grafo[posicao_w][posicao_v] != self.inf:
        self.grafo[posicao_v][posicao_w] = self.inf
        self.grafo[posicao_w][posicao_v] = self.inf
        self.m -= 1
     
    else:
      print("\n>>>Um dos locais inseridos é inexistente")

  
  def conexo(self):
    visitado = [False] * self.n
    self.dfs(0, visitado)
    if all(visitado):
      return 1
    else: 
      return 0

  def dfs(self, v, visitado):
    visitado[v] = True
    for i in range(self.n):
      if self.grafo[v][i] != self.inf and not visitado[i]:
        self.dfs(i, visitado)

  def gravarDados(self):
    os.remove("grafo.txt")
    with open("grafo.txt", "w") as arquivo:
      for i in range(len(self.vertices)+2):
        if i == 0:
          arquivo.write("2\n")
        elif i == 1:
          arquivo.write(f"{self.n}\n")
        else:
          arquivo.write(f'"{self.vertices[i-2].local}" "{self.vertices[i-2].estacao}"\n')
      arquivo.write(f"{self.m}\n")
      aux = [linha[:] for linha in self.grafo]
      for i in range(self.n):
        for j in range(self.n):
          if aux[i][j] != self.inf:
            peso = self.grafo[i][j]
            arquivo.write(f"{self.vertices[i].local}, {self.vertices[j].local}, {peso}\n")
            aux[j][i]=self.inf
      arquivo.close()
          
        
  def grauVertice(self, local):
    posicao_vertice = self.indiceNome(local)
    if posicao_vertice != -1:
      grau = 0
      for i in range(self.n):
        if self.grafo[posicao_vertice][i] != self.inf:
          grau += 1
      return grau
    else:
      return None
  
  def show(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}\n")
    for i in range(self.n):
      for j in range(self.n):
        if self.grafo[i][j] != self.inf:
          print(f"{self.vertices[i].local}  ---> {self.vertices[j].local} || DISTANCIA = {self.grafo[i][j]}km")
      print("\n")
     
  def minDistancia (self, distancias, visitado):
    min_distancia = self.inf
    min_indice = -1
    for i in range(self.n):
      if distancias[i] < min_distancia and not visitado[i]:
        min_distancia = distancias[i]
        min_indice = i
    return min_indice

  def reconstruirCaminho(self, caminho, origem, destino):
    resultado = []
    atual = destino
    while atual != -1:
      resultado.insert(0, atual)
      atual = caminho[atual]
    if resultado[0] == origem:
      return resultado
    else:
      return []

  def dijkstra(self, origem, destino):
    if self.indiceNome(origem) != -1 and self.indiceNome(origem):
      distancias = [self.inf] * self.n
      distancias[self.indiceNome(origem)] = 0
      caminho = [
          -1
      ] * self.n  
      visitado = [False] * self.n

      for _ in range(self.n):
        u = self.minDistancia(distancias, visitado)
        visitado[u] = True

        for v in range(self.n):
          if self.grafo[u][v] != self.inf and not visitado[
              v] and distancias[v] > distancias[u] + self.grafo[u][v]:
            distancias[v] = distancias[u] + self.grafo[u][v]
            caminho[v] = u

      caminho_minimo = self.reconstruirCaminho(caminho,
                                               self.indiceNome(origem),
                                               self.indiceNome(destino))
      soma_rotulos = sum(self.grafo[caminho_minimo[i]][caminho_minimo[i + 1]]
                         for i in range(len(caminho_minimo) - 1))

      caminho_minimo_objetos = [
          self.vertices[indice].estacao for indice in caminho_minimo
      ]
      print(f"\nAs estacões de {origem} até {destino} é: ")
      for i in range(len(caminho_minimo_objetos)):
        print(caminho_minimo_objetos[i], end="")
        if i < len(caminho_minimo_objetos) - 1:
          print(" -> ", end="")
      print("\nO menor caminho tem {:.2f}km".format(soma_rotulos))
    else:
      print("\n>>>Um dos locais inseridos é inexistente")

  def kruskal(self):
    arestas = []
    for i in range(self.n):
      for j in range(i + 1, self.n):
        if self.grafo[i][j] != self.inf:
          arestas.append((i, j, self.grafo[i][j]))

    arestas.sort(key=lambda x: x[2])

    conjuntos_disjuntos = [{i} for i in range(self.n)]
    arvore_minima = []
    soma_pesos = 0

    for aresta in arestas:
      vertice1, vertice2, peso = aresta
      conjunto_vertice1 = None
      conjunto_vertice2 = None

      for conjunto in conjuntos_disjuntos:
        if vertice1 in conjunto:
          conjunto_vertice1 = conjunto
        if vertice2 in conjunto:
          conjunto_vertice2 = conjunto

      if conjunto_vertice1 != conjunto_vertice2:
        arvore_minima.append(
            (self.vertices[vertice1], self.vertices[vertice2], peso))
        soma_pesos += peso
        conjunto_vertice1.update(conjunto_vertice2)
        conjuntos_disjuntos.remove(conjunto_vertice2)
        
    return arvore_minima, soma_pesos
  
