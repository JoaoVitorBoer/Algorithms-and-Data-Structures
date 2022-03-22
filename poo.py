class Node:
    def __init__(self, sozinha, sequencia, first):
        self.sozinha = sozinha
        self.sequencia = sequencia
        self.first = first


sozinhas = []
sequencia = []
vet = []
salva = 0

def somador(inicial, vet):
    achou = True
    for i in inicial: 
        for j in range(len(vet)):    
                if i == vet[j].sozinha:
                    achou = False
                    teste = inicial.replace(i, vet[j].sequencia)
                    somador(teste, vet)
    if achou == True:
      return inicial 
            
            
       
with open('caso04', 'r') as arquivo:
    vet = [Node(line[0], line[2:-1], True)  for line in arquivo.readlines() if line[0] != "\n"]
    
    for i in range(len(vet)):
        for j in range(len(vet)):
            if vet[j].sozinha in vet[i].sequencia:
               vet[j].first = False
        
  
    for i in range(len(vet)):
        if vet[i].first == True:
           salva2 = somador(vet[i].sequencia, vet)
           break

    soma = 0
    for i in range(salva2):
        soma = soma + 1

    print(soma)
            


            
    
    
        