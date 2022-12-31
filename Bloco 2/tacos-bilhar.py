# exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2016/f1/tacos-bilhar/

n_input = int(input())
c_input = input().split(" ")
stock = []
output = 0

for i in c_input:
    if i in stock:
        stock.remove(i)
    else:
        stock.insert(0, i)
        stock.insert(0, i)
        output += 2

print(output)