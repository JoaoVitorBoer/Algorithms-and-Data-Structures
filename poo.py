class Node:
    def __init__(self, sozinha, sequencia):
        self.sozinha = sozinha
        self.sequencia = sequencia






sozinhas = []
sequencia = []
teste = []

with open('caso01.txt', 'r') as arquivo:
   
    teste = [Node(line[0], line[2:]) for line in arquivo.readlines()]
    

print(teste[2].sozinha)


