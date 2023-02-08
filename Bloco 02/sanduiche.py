# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2016/f1/sanduiche/

def sum_values(values):
    sum_output = 0
    for i in values:
        sum_output += i
    return sum_output


N_ocurrences, D_objective = [int(i) for i in input().split(" ")]
ocurrences = [int(i) for i in input().split(" ")]
output = 0

for i in range(N_ocurrences):
    i_sum = sum_values(ocurrences[:i+1])
    for j in range(i, N_ocurrences):
        j_sum = sum_values(ocurrences[j:])
        sum1 = i_sum + j_sum

        sum2 = sum_values(ocurrences[i: j+1])

        if sum1 == D_objective:
            output += 1
        if sum2 == D_objective:
            output += 1

print(output)
