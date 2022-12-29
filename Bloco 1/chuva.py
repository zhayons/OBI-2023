# exercicio de: https://olimpiada.ic.unicamp.br/pratique/p2/2016/f1/chuva/

section = int(input())
values = [int(input()) for i in range(section)]
output = 0

while len(values) > 2:
    indice = 0
    for i in range(1, len(values)):
        if values[i] >= values[0]:
            indice = i
            output += len(values[0:i + 1]) - 2
            break

    del values[0:indice + 1]

print(output)
