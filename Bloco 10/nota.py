# exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2019/f1/nota/

N = int(input()) + int(input())

if N < 160:
    output = 2
elif N > 160:
    output = 1
else:
    output = 0

print(output)
