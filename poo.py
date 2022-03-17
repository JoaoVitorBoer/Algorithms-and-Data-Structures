class Node:
    def __init__(self, sozinha, sequencia):
        self.sozinha = sozinha
        self.sequencia = sequencia






sozinhas = []
sequencia = []
teste = []

with open('caso01.txt', 'r') as arquivo:
   
   # teste = [Node(line[0], line[2:])  for line in arquivo.readlines() if line[1] != "/n"]
    for line in arquivo.readlines():
        
        if line[2] != '\n':
           teste.append(Node(line[0], line[2:]))
    
   

    for i in range(len(teste)):
        print(teste[i].sozinha)


