# To what floor do the instructions take Santa?

with open('input.txt', 'r') as f:
    text = f.readlines()

floor = 0

for lines in text:
    for character in lines:

        # Go up one floor
        if character == '(':
            floor += 1

        # Go down one floor
        elif character == ')':
            floor -= 1

print(floor)