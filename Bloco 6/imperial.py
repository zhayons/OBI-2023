# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/imperial/

def valida_sequencia(items):
    validos = 1
    comparacao = items[0]
    for i in items[1:]:
        if i != comparacao + 1:
            comparacao = i
            validos += 1
    return validos


def conta_ocorrencia(items):
    posicoes = []
    for i in range(N_sequencia):
        if sequencia[i] in items:
            posicoes.append(i)

    N_posicoes_validas = valida_sequencia(posicoes)

    return N_posicoes_validas


N_sequencia = int(input())
sequencia = [int(input()) for i in range(N_sequencia)]

valores_unicos = []
output = 0

for i in range(N_sequencia):
    if sequencia[i] not in valores_unicos:
        valores_unicos.append(sequencia[i])

N_valores_unicos = len(valores_unicos)
for i in range(N_valores_unicos):
    for j in range(i, N_valores_unicos):
        i_sequencia = conta_ocorrencia([valores_unicos[i], valores_unicos[j]])
        if i_sequencia > output:
            output = i_sequencia

print(output)
