class Node:
    def __init__(self, sozinha, sequencia, first):
        self.sozinha = sozinha
        self.sequencia = sequencia
        self.first = first


sozinhas = []
sequencia = []
vet = []
salva = 0


with open('caso01', 'r') as arquivo:
    vet = [Node(line[0], line[2:-1], True)  for line in arquivo.readlines() if line[2] != "\n"]
    
    for i in range(len(vet)):
        for j in range(len(vet)):
            if vet[j].sozinha in vet[i].sequencia:
               vet[j].first = False
             
  
  
    for i in range(len(vet)):
        print(vet[i].first)
