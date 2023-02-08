# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/soma/

N_sequencia, soma_desejada = [int(i) for i in input().split(' ')]
sequencia = [int(i) for i in input().split(' ')]
output = 0

for i in range(N_sequencia):
    somatorio = 0
    for j in range(i, N_sequencia):
        somatorio += sequencia[j]
        if somatorio == soma_desejada:
            output += 1
        elif somatorio > soma_desejada:
            break

print(output)
