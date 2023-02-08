#  Exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2016/f1/toca-saci/

lines, columns = [int(i)-1 for i in input().split(" ")]
rooms = []
for i in range(lines+1):
    line = input().split(" ")
    if "3" in line:
        position = [i, line.index("3")]
    rooms.append(line)
output = 1

while rooms[position[0]][position[1]] != "2":
    print(position[0], position[1])
    if position[1] > 0:
        if rooms[position[0]][position[1]-1] == "1" or rooms[position[0]][position[1]-1] == "2":
            rooms[position[0]][position[1]] = "0"
            position[1] -= 1
            output += 1
            continue

    if position[1] < columns:
        if rooms[position[0]][position[1]+1] == "1" or rooms[position[0]][position[1]+1] == "2":
            rooms[position[0]][position[1]] = "0"
            position[1] += 1
            output += 1
            continue

    if position[0] > 0:
        if rooms[position[0]-1][position[1]] == "1" or rooms[position[0]-1][position[1]] == "2":
            rooms[position[0]][position[1]] = "0"
            position[0] -= 1
            output += 1
            continue

    if position[0] < lines:
        if rooms[position[0]+1][position[1]] == "1" or rooms[position[0]+1][position[1]] == "2":
            rooms[position[0]][position[1]] = "0"
            position[0] += 1
            output += 1
            continue

print(output)
# print(*rooms, position, columns, sep="\n")
