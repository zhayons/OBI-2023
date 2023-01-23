# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2020/f1/camisetas/

N_sequencia = int(input())
somatorio = 0
for i in input().split(' '):
    somatorio += int(i)
N_p = int(input())
N_m = int(input())

output = 'S' if (N_p + N_m*2) == somatorio else 'N'
print(output)
