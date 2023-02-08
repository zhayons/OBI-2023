# exercíciode: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/pandemia/

def add_infectados(novos_infectados):
    for i in novos_infectados:
        if i not in infectados:
            infectados.append(i)


N_amigos, N_reunioes = [int(i) for i in input().split(' ')]
infectado, data_infectado = [int(i) for i in input().split(' ')]
reunioes = []
for i in range(N_reunioes):
    reunioes.append([int(i) for i in input().split(' ')[1:]])
infectados = reunioes[data_infectado-1]

for i in reunioes[data_infectado:]:
    for j in i:
        if j in infectados:
            add_infectados(i)
            break

output = len(infectados)
print(output)
