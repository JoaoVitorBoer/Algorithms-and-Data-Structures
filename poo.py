class Node:
    def __init__(self, sozinha, sequencia, first):
        self.sozinha = sozinha
        self.sequencia = sequencia
        self.first = first


sozinhas = []
sequencia = []
vet = []
salva = 0

def somador(inicial, vet, soma_parcial):
    soma = soma_parcial
    achou = True
    for i in inicial: #m e m i m o m u
        for j in range(len(vet)): 
           if i == vet[j].sozinha: #vv uu -> funcionando corretamente               
               achou = False
               soma = soma + len(vet[j].sequencia)
               teste = inicial.replace(i, vet[j].sequencia)               
               somador(teste, vet, soma)
           
    if achou == True:
      return soma
            
            
       
with open('caso01', 'r') as arquivo:
    vet = [Node(line[0], line[2:-1], True)  for line in arquivo.readlines() if line[2] != "\n"]
    
    for i in range(len(vet)):
        for j in range(len(vet)):
            if vet[j].sozinha in vet[i].sequencia:
               vet[j].first = False
        
  
    for i in range(len(vet)):
        if vet[i].first == True:
           salva2 = somador(vet[i].sequencia, vet, len(vet[i].sequencia))
           
           break
    print(salva2)
    
    
            


            
    
    
        