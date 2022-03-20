class Linhas:
  def __init__(self,letra,palavra,primeiro,valor):
    self.letra = letra
    self.palavra = palavra
    self.primeiro = primeiro
    self.valor=valor

def Soma(vetor,letrinha):
  soma=0
  achou = False
  for i in range(len(vetor)):
    if(vetor[i].letra==letrinha):
      if vetor[i].valor == 0:
        #print(vetor[i].letra)
        achou=True
        for j in range(len(vetor[i].palavra)):
          #if vetor[i].valor!=0:
          soma+=Soma(vetor,vetor[i].palavra[j])
        vetor[i].valor=soma
        #print(vetor[i].letra," ",vetor[i].palavra,"=",vetor[i].valor)
        i=len(vetor)
      else: 
        achou=True
        soma=vetor[i].valor
  if (achou==False and letrinha!= '\n'):
    #print(letrinha)
    #print("somou")
    soma=1
  return soma


#Guarda as letras e as palavras em um vetor
with open('caso01','r')as arquivo:
  vetor= []
  for line in arquivo:
    if (line[2]) != '\n':
      #print (line[0])
      #print (line[2:])
      vetor.append((Linhas(line[0],line[2:], True,0)))
  
  

#Demarca qual é o inicial
for i in range(len(vetor)):#vetor das palavras
  for x in range(len(vetor)):#vetor das letras
    if vetor[x].letra in vetor[i].palavra:
     # print(f'Vetor[i]: {vetor[i].palavra[j]}')
     # print(f'Vetor[x]: {vetor[x].letra}')
      #if vetor[x].letra==(vetor[i].palavra[j]):
          vetor[x].primeiro=False
        #print(vetor[x].primeiro)   

#Encontra o primeiro char da linha inicial
soma=0
for i in range(len(vetor)): 
  if vetor[i].primeiro==True:
    #print(vetor[i].letra)
    #print("")
    for j in range(len(vetor[i].palavra)):
      #print(vetor[i].palavra[j])
      soma+=Soma(vetor,vetor[i].palavra[j])

print(soma)