def print_path(lista):
    with open('path.txt', 'a', newline='') as file:
        for x in lista:
            for y in x:
             file.write(str(y)+' ')
            
            file.write('\n')
    