# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2018/f1/figurinhas/

N_figurinhas, N_carimbadas, N_compradas = input().split(" ")
carimbadas = input().split(" ")
compradas = input().split(" ")
output = int(N_carimbadas)

for i in carimbadas:
    if i in compradas:
        output -= 1

print(output)
