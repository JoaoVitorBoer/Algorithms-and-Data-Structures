class Node:
    def __init__(self, sozinha, sequencia):
        self.sozinha = sozinha
        self.sequencia = sequencia






sozinhas = []
sequencia = []
teste = []

with open('caso01.txt', 'r') as arquivo:
    linhas = [line.rstrip() for line in arquivo.readlines()]
    for palavra in linhas:
        teste.append(Node(palavra[0], palavra[2:]))
        sozinhas.append(palavra[0])
        sequencia.append(palavra[2:])

#print(sozinhas)
#print(sequencia)
print(teste[1].sozinha)


