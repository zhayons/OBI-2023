# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2019/f1/idade/

monica = int(input())
filho_1 = int(input())
filho_2 = int(input())
filho_3 = monica - filho_1 - filho_2
output = filho_1

if filho_2 > output:
    output = filho_2
if filho_3 > output:
    output = filho_3

print(output)

