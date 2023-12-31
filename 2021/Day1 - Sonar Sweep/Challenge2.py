# Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

with open('input.txt', 'r') as f:
    text = f.readlines()

# Get the initial 3 sum values and remove first line
value = int(text.pop(0)) + int(text[1]) + int(text[2])
increases = 0

for i in range(len(text) - 2):

    if value < int(text[i]) + int(text[i + 1]) + int(text[i + 2]):
        increases += 1

    value = int(text[i]) + int(text[i + 1]) + int(text[i + 2])

print(increases)