# exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2019/f1/amigos/

N_sequencia = int(input())
sequencia = [int(i) for i in input().split(' ')]
output = 0

for i in range(N_sequencia):
    for j in range(N_sequencia):
        soma_caminho = sequencia[i] + sequencia[j] + (j-i)
        if soma_caminho > output:
            output = soma_caminho

print(output)
