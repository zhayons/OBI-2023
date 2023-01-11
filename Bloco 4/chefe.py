"""# Exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/chefe/
###
def min_idade(gerentes):
    if gerentes == []:
        idade = "*"
    else:
        idade = empregados_troca[gerentes[0]]
        for i in gerentes[1:]:
            if empregados_troca[i] < idade:
                idade = empregados_troca[i]
    return idade


def troca_gerentes(posicoes):
    for i in range(N_empregados):
        empregados_troca[i] = empregados[i]
    temp = empregados[posicoes[0]]
    empregados_troca[posicoes[0]] = empregados[posicoes[1]]
    empregados_troca[posicoes[1]] = temp


N_empregados, N_relacoes, N_operacoes = [int(i) for i in input().split(" ")]
empregados = [int(i) for i in input().split(" ")]
empregados_troca = empregados.copy()
relacoes = [[] for i in range(N_empregados)]
output = ""

for i in range(N_relacoes):
    gerente, gerenciado = [int(i)-1 for i in input().split(" ")]
    relacoes[gerenciado].append(gerente)
    for j in relacoes[gerente]:
        if j not in relacoes[gerenciado]:
            relacoes[gerenciado].append(j)

# for i in range(N_operacoes):
#     operacao = input().split(" ")
#     if operacao[0] == "P":
#         funcionario = int(operacao[1]) - 1
#         output += str(min_idade(relacoes[funcionario])) + "\n"
#     else:
#         funcionarios = (int(operacao[1]) - 1, int(operacao[2]) - 1)
#         troca_gerentes(funcionarios)

print(empregados_troca, relacoes, sep="\n")
print(min_idade(relacoes[7-1]))
troca_gerentes((4-1, 2-1))
print(empregados_troca, relacoes, sep="\n")
print(min_idade(relacoes[7-1]))
print(min_idade(relacoes[5-1]))
troca_gerentes((1-1, 4-1))
print(empregados_troca, relacoes, sep="\n")
print(min_idade(relacoes[7-1]))
troca_gerentes((4-1, 7-1))
print(empregados_troca, relacoes, sep="\n")
print(min_idade(relacoes[2-1]))
print(min_idade(relacoes[6-1]))

# print(output)"""