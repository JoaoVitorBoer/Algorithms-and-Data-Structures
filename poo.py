class Node:
    def __init__(self, sozinha, sequencia, first, tamanho):
        self.sozinha = sozinha
        self.sequencia = sequencia
        self.first = first
        self.tamanho = tamanho


sozinhas = []
sequencia = []
vet = []
salva = 0

def somador(inicial, vet):

    achou = True
    for i in inicial: #m e m i m o m u
        for j in range(len(vet)): 
            if inicial == vet[j].sozinha: #vv uu -> funcionando corretamente 
               if vet[j].tamanho == 0:              
                achou = False
                for x in vet[j].sequencia:
                 soma = soma + somador(x, vet)
                vet[j].tamanho = soma
                z = len(vet)
            else:
                achou = False
                soma = vet[j].tamanho
    if(achou == False and i !='\n'):
        soma = 1
    return soma
            
            
       
with open('caso01', 'r') as arquivo:
    vet = [Node(line[0], line[2:-1], True, 0)  for line in arquivo.readlines() if line[2] != "\n"]
    
    for i in range(len(vet)):
        for j in range(len(vet)):
            if vet[j].sozinha in vet[i].sequencia:
               vet[j].first = False
        
    salva2 = 0
    for i in range(len(vet)):
        if vet[i].first == True:
            salva2 +=  somador(vet[i].sequencia, vet)           
    
    print(salva2)
    
    
            


            
    
    
        