code_lines = int(input())

code = ""
output = 0

for i in range(code_lines):
    code += input()

for i in code:
    if i == "{":
        output += 1
    elif i == "}":
        output -= 1

output = "S" if output == 0 else "N"
print(output)
