import re

# Part 1
input = r"C:\Users\kunfu\OneDrive\Documents\input3.txt"
with open(input, 'r') as file: 
    lines = file.read()

def mul(x, y):
    return x * y

check = r"mul\((\d{1,3}),(\d{1,3})\)"

sum = 0
for i, line in enumerate(lines.splitlines()): 
    same = re.findall(check, line)
    for match in same:
        x, y = int(match[0]), int(match[1])
        result = mul(x, y)
        sum += result
print("Part 1:", sum)

# Part 2

do_check = re.compile(r"do\(\)")
dont_check = re.compile(r"don't\(\)")
sum2 = 0
enable = True
split = re.split(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", lines)

for line in split:
    if re.search(do_check, line):
        enable = True
    elif re.search(dont_check, line):
        enable = False
    if enable:
        same = re.findall(check, line)
        for match in same:
            x, y = int(match[0]), int(match[1])
            result = mul(x, y)
            sum2 += result
print("Part 2:", sum2)
