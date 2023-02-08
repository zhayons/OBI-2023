# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2018/f1/piso/

N_largura = int(input())
N_comprimento = int(input())
output_1 = (N_largura-1) * (N_comprimento-1) + N_largura * N_comprimento
output_2 = (N_largura-1) * 2 + (N_comprimento-1) * 2

print(output_1, output_2, sep="\n")
