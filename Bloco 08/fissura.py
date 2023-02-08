# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/fissura/

def espalha():
    mudou = False
    for i in range(N_matriz):
        if mudou:
            True
        for j in range(N_matriz):
            if matriz[i][j] != '*':
                is_adjacente = (
                    (i > 0 and matriz[i-1][j] == '*') or
                    (i < N_matriz-1 and matriz[i+1][j] == '*') or
                    (j > 0 and matriz[i][j-1] == '*') or
                    (j < N_matriz-1 and matriz[i][j+1] == '*')
                )
                if is_adjacente and matriz[i][j] <= forca:
                    matriz[i][j] = '*'
                    mudou = True
    return mudou



N_matriz, forca = [int(i) for i in input().split(' ')]
matriz = []
for i in range(N_matriz):
    matriz.append([int(j) for j in input()])

if matriz[0][0] <= forca:
    matriz[0][0] = '*'
    flag = True
    while flag:
        flag = espalha()


for i in matriz:
    print(*i, sep='')
