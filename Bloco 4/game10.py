# exercício de:

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
