input_1 = int(input())
input_2 = [int(i) for i in input().split(" ")]

members_sum = input_2[0] + input_2[1] + input_2[2] + input_2[6] - input_2[3] - input_2[4] - input_2[5]

out_value = "N" if members_sum <= input_1 else "S"
print(out_value)
S