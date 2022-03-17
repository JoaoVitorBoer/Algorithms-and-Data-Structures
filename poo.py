class Node:
    def __init__(self, sozinha, sequencia):
        self.sozinha = sozinha
        self.sequencia = sequencia


sozinhas = []
sequencia = []
vet = []

with open('caso01.txt', 'r') as arquivo:
    vet = [Node(line[0], line[2:-1])  for line in arquivo.readlines() if line[2] != "\n"]
    
   

    


