# exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2017/f1/cofre/

N_sequence = int(input().split(" ")[0])
sequence = [int(i) for i in input().split(" ")]
positions = [int(i) for i in input().split(" ")]
key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
position = -1

for i in positions:
    if i-1 > position:
        for j in range(position+1, i):
            key[sequence[j]] += 1
    else:
        for j in range(position-1, i-2, -1):
            key[sequence[j]] += 1
    position = i - 1

print(key)
