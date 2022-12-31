# exercício de : https://olimpiada.ic.unicamp.br/pratique/p2/2016/f1/lampadas-hotel/

A, B, Af, Bf = input().split(" ")
A = int(A)
B = int(B)
Af = int(Af)
Bf = int(Bf)
output = 0

if (A, B) != (Af, Bf):
    if (A, not B) == (Af, Bf):
        output = 2
    else:
        output = 1

print(output)
