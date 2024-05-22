"Caio Eduardo Todesco Gomes RA: 10358993"
import Arquivo
from aresta import Aresta
from aresta import Vertice
from Matriz import GrafoMatND

importGrafo = True


def menu(opcao):
  global grafo, importGrafo
  if opcao == 1:  
    if importGrafo == True:
      grafo = Arquivo.leArquivoMatriz()
      importGrafo = False
    else:
      print("O arquivo txt já foi inserido no grafo.")      

  elif opcao == 2:  #Grava grafo atual no arquivo
    if importGrafo == False:
      grafo.gravarDados()
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 3:
    if importGrafo == False:
      nome_local = input("Insira um nome para o local onde deseja ir: ").upper()
      nome_estacao = input("Insira um nome para a estacao que você deseja começar: ").upper()
      vertice = Vertice(nome_local, nome_estacao)
      grafo.insereVertice(vertice)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")   

  elif opcao == 4:
    if importGrafo == False:
      aresta_origem = input("Insira o local de origem: ").upper()
      aresta_destino = input("Insira o local de destino: ").upper()
      peso = float(input("Insira o valor do peso: "))
      grafo.insereA(aresta_origem, aresta_destino, peso)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 5:
    if importGrafo == False:
      nome_local = input("Insira o local que deseja remover: ").upper()
      grafo.removerVertice(nome_local)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 6:
    if importGrafo == False:
      aresta_origem = input(
          "Digite o local de origem que deseja remover da aresta: ").upper()
      aresta_destino = input(
          "Digite o local de destino que deseja remover da aresta: ").upper()
      grafo.removeA(aresta_origem, aresta_destino)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 7:
    if importGrafo == False:
      print("Mostrando o conteúdo do arquivo txt:\n")
      with open("grafo.txt", "r") as arquivo:
        linhas = arquivo.read()
        print(linhas)
      arquivo.close()
    else: 
      print("Primeiramente, insira os dados no grafo (opção 1)")
      

  elif opcao == 8:
    if importGrafo == False:
      grafo.show()
    else: 
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 9:
    if importGrafo == False:
      if grafo.conexo() == 1:
        print("O Grafo de locais e estações de metrô é conexo.\n")
      elif grafo.conexo() == 0:
        print("O Grafo de locais e estações de metrô é desconexo.\n")
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")
        
  elif opcao == 10:
    if importGrafo == False:
      origem = input("Digite o local de origem: ").upper()
      destino = input("Digite o local de destino: ").upper()
      grafo.dijkstra(origem, destino)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 11:
    if importGrafo == False:
      local = input("Digite o local para saber o grau dele: ").upper()
      grau = grafo.grauVertice(local)
      if grau is not None:
        print(f'O grau do local {local} é {grau}')
      else:
        print("\nO local inserido é inexistente")
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")
      
  elif opcao == 12:
    if importGrafo == False:
      arvore_minima, soma_pesos = grafo.kruskal()
  
      print("\nÁrvore Geradora Mínima:")
      for aresta in arvore_minima:
        local1, local2, peso = aresta
        print(f"{local1.local} --- {local2.local} || PESO = {peso} km")
      print(f"\nA soma dos pesos da Árvore Geradora Mínima é {soma_pesos:.2f} km")
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")


def main():
  while True:
    print("\n-------------- GRAFO PONTOS TURISTICOS --------------\n")
    print("1 - Ler dados do arquivo grafo.txt")
    print("2 - Gravar dados no arquivo grafo.txt")
    print("3 - Inserir vértice")
    print("4 - Inserir aresta")
    print("5 - Remove vértice")
    print("6 - Remove aresta")
    print("7 - Mostrar conteúdo do arquivo")
    print("8 - Mostrar grafo")
    print("9 - Apresentar a conexidade do grafo")
    print("10 - Caminho minino")
    print("11 - Grau do vertice")
    print("12 - Árvore de custo minimo")
    print("0 - Encerrar a aplicação\n")

    opcao = int(input("Selecione uma opção do menu: "))
    if opcao == 0:
      break
    menu(opcao)


main()

