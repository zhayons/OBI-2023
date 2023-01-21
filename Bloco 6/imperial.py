# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/imperial/

def ocorrencias(item):
    count = 0
    item_posicoes = []
    for i in range(N_sequencia):
        if sequencia[i] == item:
            count += 1
            item_posicoes.append(i)
    return count, item_posicoes


N_sequencia = int(input())
sequencia = [int(input()) for i in range(N_sequencia)]

valores_unicos = []
output = 0

for i in range(N_sequencia):
    if sequencia[i] not in valores_unicos:
        valores_unicos.append(sequencia[i])
        i_ocorrencias, i_posicoes = ocorrencias(sequencia[i])
        if output <= i_ocorrencias:
            for j in range(i+1, N_sequencia):
                if sequencia[j] not in
            output = i_ocorrencias

print(N_sequencia, sequencia)
print(ocorrencias(10), posicoes)
print(valores_unicos)
