import numpy as np
import time

def cria_matriz(arquivo):

  vet = []
  for linha in arquivo:
    for char in linha:
      if char != "\n":
        vet.append(char)
      
  tamanho_matriz = len(arquivo)
  matriz = []
  while vet != []:
    matriz.append(vet[:tamanho_matriz])
    vet = vet[tamanho_matriz:]

  return matriz, tamanho_matriz

  

def cria_aux(tamanho_tabuleiro):
  matrix = np.zeros((tamanho_tabuleiro, tamanho_tabuleiro), dtype = bool)
  return matrix
  


def encontra_players(tabuleiro, tamanho):

  vet_players = []
  num = [1,2,3,4,5,6,7,8,9]
  for x in range(tamanho):
    for j in range(tamanho):
      if tabuleiro[x][j] in str(num):
        vet_players.append((tabuleiro[x][j],x,j))
        if len(vet_players) == 9: 
          return vet_players
    
     

  
def posicoesParaVisitar(p, tamanho_tabuleiro):
  posicoes = []
  if (p[0]-1 or p[1]+0) > tamanho_tabuleiro:
      posicoes.append([p[0], p[1]])
  else:
      posicoes.append([p[0]-1, p[1]+0])

  if (p[0]+1 or p[1]+0) > tamanho_tabuleiro:
    posicoes.append([p[0], p[1]])
  else:  
    posicoes.append([p[0]+1, p[1]+0]) 

  if (p[0]+0 or p[1]-1) > tamanho_tabuleiro:
    posicoes.append([p[0], p[1]])
  else:
    posicoes.append([p[0]+0, p[1]-1])

  if (p[0]+0 or p[1]+1) > tamanho_tabuleiro:
    posicoes.append([p[0], p[1]])
  else:
    posicoes.append([p[0]+0, p[1]+1])

  return posicoes



  
  
def buscaemLargura(tabuleiro, tamanho_tabuleiro, posicao, tabuleiro_aux):

  list = []
  x = [posicao[0], posicao[1], 0]
  
  
  list.append(x) #coloca a primeira posicao na fila
  num = [1,2,3,4,5,6,7,8,9]
  tabuleiro_aux[x[0]][x[1]] = True

  soma = 1
  chaves = []
  portas = []
  
  while len(list) > 0:
    p = list[0]    #pega a primeira posicao da fila
    #print(p)
    list.remove(p)
    proximasPosicoes = posicoesParaVisitar(p, tamanho_tabuleiro) #Array com prox posicoes
    for i in range(4):
      
      p2 = proximasPosicoes[i] #Lembrando que aqui é uma tupla [(x,y)]

      if tabuleiro[p2[0]][p2[1]] == "." and tabuleiro_aux[p2[0]][p2[1]] == False:
        y = [p2[0], p2[1]]
        list.append(y)
        tabuleiro_aux[p2[0]][p2[1]] = True
        soma = soma+1
        
      #pegando se o caracter por exemplo 'c' por exemplo for encontrado
      if tabuleiro[p2[0]][p2[1]].isalpha() == True and tabuleiro[p2[0]][p2[1]].islower() == True and tabuleiro_aux[p2[0]][p2[1]] == False:

        #print(f'Pegou a chave {tabuleiro[p2[0]][p2[1]]}')
        y = [p2[0], p2[1]]
        list.append(y)
        tabuleiro_aux[p2[0]][p2[1]] = True
        soma = soma+1
        chaves.append(tabuleiro[p2[0]][p2[1]])
        
        for i in range(len(portas)):
          if tabuleiro[p2[0]][p2[1]].upper() == portas[i][0]:
              aux = [portas[i][1], portas[i][2], 0]     #  Adiciona a posição na porta
              list.append(aux)
              soma = soma +1
              tabuleiro_aux[portas[i][1]][portas[i][2]] = True
              #print(f'Adicionou a lista a porta {aux} para ser aberta')
              
        

      #pegando portas
      if tabuleiro[p2[0]][p2[1]].isalpha() == True and tabuleiro[p2[0]][p2[1]].isupper() == True and tabuleiro_aux[p2[0]][p2[1]] == False:
        if tabuleiro[p2[0]][p2[1]].lower() in chaves: #Se abriu conta na soma +1
          y = [p2[0], p2[1]]
          #print(f'Abriu {tabuleiro[p2[0]][p2[1]]} posicao{p2[0], p2[1]} e somou 1')
          tabuleiro_aux[p2[0]][p2[1]] = True
          list.append(y)
          soma = soma+1
         
        elif [tabuleiro[p2[0]][p2[1]], p2[0], p2[1]] not in portas:
          portas.append([tabuleiro[p2[0]][p2[1]], p2[0], p2[1]])  #Tupla


      #Se encontrar outros players
      if tabuleiro[p2[0]][p2[1]] in str(num) and tabuleiro_aux[p2[0]][p2[1]] == False:
        y = [p2[0], p2[1]]
        list.append(y)
        tabuleiro_aux[p2[0]][p2[1]] = True
        soma = soma+1

  
  return soma
vet = ['05','06','07','08','09','10']
for x in vet:
  print(f'----------------------------------------------')
  print(f'Executando o caso{x} \n')
  with open('caso'+x, 'r') as file:
    ini = time.time()
    arquivo = file.readlines()
    
    print(f'Tamanho do arquivo: {len(arquivo)} \n')
    tabuleiro, tamanho_tabuleiro = cria_matriz(arquivo)
    tabuleiro_aux = cria_aux(tamanho_tabuleiro)
  
    players_pos = encontra_players(tabuleiro, tamanho_tabuleiro)
    players_pos.sort()
    print(f'Posições dos players {players_pos} \n')
    
    
    for posicao in players_pos:
     posicao_noTabuleiro = (posicao[1], posicao[2])
     resultado= buscaemLargura(tabuleiro, tamanho_tabuleiro, posicao_noTabuleiro, tabuleiro_aux)
     tabuleiro_aux = cria_aux(tamanho_tabuleiro)
     print(f'Player {posicao[0]} pode andar {resultado} casas')
     fim = time.time()
     
  print(f'\nTempo {fim-ini} \n')

