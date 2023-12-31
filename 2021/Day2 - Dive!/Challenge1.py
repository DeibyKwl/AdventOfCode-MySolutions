# What do you get if you multiply your final horizontal position by your final depth?

with open('input.txt', 'r') as f:
    text = f.readlines()

horizontal = 0
depth = 0

for line in text:

    line = line.split()

    if 'forward' in line:
        horizontal += int(line[1])

    elif 'down' in line:
        depth += int(line[1])
        
    elif 'up' in line:
        depth -= int(line[1])

print(horizontal * depth)