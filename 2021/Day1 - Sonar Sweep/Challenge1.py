# How many measurements are larger than the previous measurement?

with open('input.txt', 'r') as f:
    text = f.readlines()

# Get rid of first measurement
value = int(text.pop(0)) 
increases = 0

for line in text:

    if value < int(line):
        increases += 1

    value = int(line)

print(increases)