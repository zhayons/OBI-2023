# exercício de: https://olimpiada.ic.unicamp.br/pratique/p2/2017/f1/botas/

N_boots = int(input())
left = []
right = []
output = 0

for i in range(N_boots):
    boot_num, boot_side = input().split(" ")
    if boot_side == "E":
        if boot_num in right:
            output += 1
            right.remove(boot_num)
        else:
            left.append(boot_num)
    else:
        if boot_num in left:
            output += 1
            left.remove(boot_num)
        else:
            right.append(boot_num)

print(output)
