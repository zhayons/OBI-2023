# exercicio de: https://olimpiada.ic.unicamp.br/pratique/p2/2016/f1/chuva/
def max_value(value):
    m_value = value[0]
    index_value = 0
    for i in range(1, len(value)):
        if value[i] >= m_value:
            m_value = value[i]
            index_value = i

    return m_value, index_value


section = int(input())
values = [int(input()) for i in range(section)]
output = 0

pre = 0
pos, pos_index = max_value(values)

for i in range(len(values)-1):
    if i == pos_index:
        pos, pos_index = max_value(values[i+1:])

    if values[i] < pre and values[i] < pos:
        output += 1

    if values[i] > pre:
        pre = values[i]

print(output)
