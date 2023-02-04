# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/promocao/

# def proximo_onibus(intinerario, cidade_atual, empresa, historico):



N_cidades = int(input())
intinerarios = []
for i in range(N_cidades-1):
    intinerarios.append([int(i) for i in input().split(' ')])
output = 0
print(N_cidades, *intinerarios, sep='\n')


