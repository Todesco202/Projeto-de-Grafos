"Caio Eduardo Todesco Gomes RA: 10358993"

class Aresta:
  def __init__(self,origem, destino, peso):
    self.vertice1 = origem
    self.vertice2 = destino
    self.peso = peso

class Vertice:
  def __init__(self, local, estacao):
    self.local = local
    self.estacao = estacao
