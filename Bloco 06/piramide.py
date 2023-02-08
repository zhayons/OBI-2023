# Exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2018/f1/piramide/

def menor_valor(valores):
    menor = valores[0]
    index = 0
    for x in range(1, len(valores)):
        if valores[x] < menor:
            menor = valores[x]
            index = x

    return menor, index


N_matriz = int(input())
matriz = []
for i in range(N_matriz):
    matriz.append([int(j) for j in input().split(" ")])

soma_colunas = []
for i in range(N_matriz):
    soma = 0
    for j in range(N_matriz):
        soma += matriz[j][i]
    soma_colunas.append(soma)

output, coluna_inicial = menor_valor(soma_colunas)
coluna_esquerda = coluna_inicial - 1
coluna_direita = coluna_inicial + 1

for i in matriz[:-1]:
    for j in range(N_matriz):
        soma_colunas[j] -= i[j]

    if coluna_esquerda >= 0:
        if coluna_direita <= N_matriz:
            menor, indice = menor_valor((soma_colunas[coluna_esquerda], soma_colunas[coluna_direita]))
            output += menor
            if indice == 0:
                coluna_esquerda -= 1
            else:
                coluna_direita += 1
        else:
            output += soma_colunas[coluna_esquerda]
            coluna_esquerda -= 1
    else:
        output += soma_colunas[coluna_direita]
        coluna_direita += 1

print(
    *matriz, "-"*10,
    soma_colunas,
    coluna_esquerda, coluna_direita,
    output,
    sep="\n ")
