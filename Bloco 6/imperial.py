# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/imperial/

def consecutivo(posicao_sequencia):

    for i in posicao_sequencia:



N_sequencia = int(input())
sequencia = [int(input()) for i in range(N_sequencia)]

valores_unicos = []
posicoes = []
output = 0

for i in range(N_sequencia):
    if sequencia[i] not in valores_unicos:
        valores_unicos.append(sequencia[i])
        i_posicoes = []
        for j in range(i, N_sequencia):
            if sequencia[i] == sequencia[j]:
                i_posicoes.append(j)
        posicoes.append(i_posicoes)

N_valores_unicos = len(valores_unicos)
for i in range(N_valores_unicos):
    N_posicoes = len(posicoes[i])
    if N_posicoes > output:
        output = N_posicoes


print(N_sequencia, sequencia)
print(valores_unicos, posicoes)
print(output)
