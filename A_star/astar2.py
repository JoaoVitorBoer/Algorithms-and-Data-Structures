from printa_maze import print_path, cria_matriz, get_comidas

def heuristica(pos, end):
    return abs(end[0] - pos[0]) +  abs(end[1] - pos[1])

def manhattan(possiveis_pos, end):    
    menor = heuristica(possiveis_pos[0], end)
    salva_tupla = ()
    for pos in possiveis_pos:
        aux = heuristica(pos, end)
        if aux < menor:
            menor = aux
            salva_tupla = pos
    print(salva_tupla)
    return salva_tupla

    
def posParaVisitar(pos_atual):
    possiveis_pos = []
    for nova_pos in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacentes
        pos = (pos_atual[0] + nova_pos[0], pos_atual[1] + nova_pos[1])
        if pos[0] >= 0 and pos[1] >= 0: 
            possiveis_pos.append(pos)
    #print(possiveis_pos)
    return possiveis_pos
    

def astar(maze, maze_aux, start, end):

    lista = []
    lista.append(start)
    maze_aux[start[0]][start[1]] = 'S'
    caminho_adequado = []
    caminho_adequado.append(start)

    while len(lista) > 0:
        
        pos = lista[0]
        lista.pop(0)
        pos_visitar = posParaVisitar(pos)
        salva_validas = []
        for posi_atual in pos_visitar:
            if maze[posi_atual[0]][posi_atual[1]] != 1:
                #maze_aux[posi_atual[0]][posi_atual[1]] = 'x'
                salva_validas.append(posi_atual)
            if posi_atual == end:
                maze_aux[posi_atual[0]][posi_atual[1]] = 'F'
                caminho_adequado.append(posi_atual)
                return caminho_adequado, maze_aux
        
        melhor_pos = manhattan(salva_validas, end)
        maze_aux[melhor_pos[0]][melhor_pos[1]] = '-'
        caminho_adequado.append(melhor_pos)
        lista.append(melhor_pos)




def main():
      with open("labirinto1.txt", 'r') as f:
        arquivo = f.readlines()
    # maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        maze = cria_matriz(arquivo)
        comidas = get_comidas(arquivo)
        maze_aux =  maze

        start = (0, 0)
        end = comidas[0]

        path, maze_aux = astar(maze, maze_aux, start, end)
        print(path)
        for x in maze_aux:
            for y in x:
                print(y, end=" ")
            print('\n')

        print_path(maze_aux)
    
if __name__ == '__main__':
    main()