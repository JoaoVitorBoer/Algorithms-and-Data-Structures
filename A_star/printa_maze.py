def print_path(lista):
    with open('path.txt', 'a', newline='') as file:
        for x in lista:
            for y in x:
             file.write(str(y)+' ')
            
            file.write('\n')


def cria_matriz(arquivo):
        vet = []
        for linha in arquivo:
            for char in linha:
                if char != "\n":
                    vet.append(char)
                
        tamanho_matriz = len(arquivo)
        matriz = []
        while vet != []:
            matriz.append(vet[:tamanho_matriz])
            vet = vet[tamanho_matriz:]

        return matriz

def get_comidas(arquivo):
    pos_comidas = []
    for i, linha in enumerate(arquivo):
        for j, char in enumerate(linha):
         if char == "C":
            pos_comidas.append((i,j))

    return pos_comidas
    