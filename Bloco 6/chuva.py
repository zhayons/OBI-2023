# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/chuva/

def substitui():
    mudou = False
    for i in range(N_i):
        for j in range(N_j):
            if matriz[i][j] == '.':
                if (
                    (i > 0 and matriz[i-1][j] == 'o') or
                    (j < N_j-1 and i < N_i-1 and matriz[i][j+1] == 'o' and matriz[i+1][j+1] == '#') or
                    (j > 0 and i < N_i-1 and matriz[i][j-1] == 'o' and matriz[i+1][j-1] == '#')
                ):
                    matriz[i][j] = 'o'
                    mudou = True
                    break
        if mudou:
            break
    return mudou


N_i, N_j = [int(i) for i in input().split(' ')]
matriz = []
for i in range(N_i):
    matriz.append([*input()])

print('\n')
incompleto = True
while incompleto:
    incompleto = substitui()

for i in matriz:
    print(*i)
