# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/game10/

NUM_positions = int(input())
MISSEL_posiition = int(input())
PLAYER_position = int(input())
output = 0

while MISSEL_posiition != PLAYER_position:
    if PLAYER_position != NUM_positions:
        PLAYER_position += 1
    else:
        PLAYER_position = 1
    output += 1

print(output)
