# exercício de: https://olimpiada.ic.unicamp.br/pratique/p1/2018/f1/escadinha/

N_sequence = int(input())
sequence = [int(i) for i in input().split(" ")]
differences = []

if N_sequence == 1:
    output = 1
elif N_sequence > 1:
    output = 0
    for i in range(N_sequence-1):
        difference = sequence[i] - sequence[i+1]
        if difference not in differences:
            differences.append(difference)
            output += 1

print(output)
