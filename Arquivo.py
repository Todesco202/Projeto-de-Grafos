"Caio Eduardo Todesco Gomes RA:10358993"
from aresta import Aresta, Vertice
from Matriz import GrafoMatND

locais = []
listaArestas = []

def leArquivoMatriz(): 
  with open("grafo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas):
      if i == 0:
        tipo_grafo = linha
      elif i == 1:
        tamanho_inicial = int(linha)
        
      else:
        if i == tamanho_inicial+2:
          qtde_arestas = linha
        elif '"' in linha:
          linha_separa = linha.split('"')
          local = linha_separa[1]
          estacao_metro = linha_separa[3]
          vertice = Vertice(local, estacao_metro)
          locais.append(vertice)
          
              
        else:
          arestas_separa = linha.split(", ")
          
          a_1 = arestas_separa[0]
          a_2 = arestas_separa[1]
          peso = arestas_separa[2]
          objeto = Aresta(a_1, a_2, float(peso))                
          listaArestas.append(objeto)
      
  grafo = GrafoMatND(len(locais))
  grafo.insereVerticeInicial(locais)
  for aresta in listaArestas:
    grafo.insereA(aresta.vertice1, aresta.vertice2, aresta.peso)      
  arquivo.close()
  return grafo
