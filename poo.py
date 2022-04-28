class Node:
    def __init__(self, sozinha, sequencia, first, tamanho):
        self.sozinha = sozinha
        self.sequencia = sequencia
        self.first = first
        self.tamanho = tamanho


sozinhas = []
sequencia = []
vet = []

def Somador(vet, letra):
  soma = 0
  for i in range(len(vet)):
    if vet[i].sozinha == letra:
      if vet[i].sequencia == False:
        return(1)
      else:
        for x in range(len(vet)):
          for z in range(len(vet)):
            soma += Somador(vet, vet[x].sequencia[z])
  return soma      
  



            
            
       
with open('caso01', 'r') as arquivo:
    vet = [Node(line[0], line[2:-1], True, int(len(line[2:-1])))  for line in  arquivo.readlines() if line[2] != "\n"]
   
    for i in range(len(vet)):
        for j in range(len(vet)):
            if vet[j].sozinha in vet[i].sequencia:
               vet[j].first = False
      
    soma = 0
    for x in range(len(vet)):
      if vet[x].first == True:
        for j in range(len(vet[x].sequencia)):
           soma += Somador(vet, vet[x].sequencia[j])

    print(soma)
   