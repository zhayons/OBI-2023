# exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2018/f1/xadrez/

N_linhas = int(input())
N_colunas = int(input())

output = 1 if (N_linhas + N_colunas) % 2 == 0 else 0
print(output)
