# Exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/3por2/

n_produtos = int(input())
produtos = [int(input())]
for i in range(n_produtos-1):
    preco = int(input())
    for j in range(i+1):
        if preco <= produtos[j]:
            produtos.insert(j, preco)
            break
        elif j == i:
            produtos.append(preco)

output = sum(produtos[:n_produtos % 3])

for i in range((n_produtos % 3), n_produtos, 3):
    output += produtos[i+1]
    output += produtos[i+2]

print(output)
