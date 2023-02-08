# exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2017/f1/teleferico/

capacity = int(input())
students = int(input())
output = students // (capacity-1)
if students % (capacity-1) != 0:
    output += 1

print(output)
