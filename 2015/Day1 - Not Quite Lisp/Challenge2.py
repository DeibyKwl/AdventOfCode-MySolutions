# What is the position of the character that causes Santa to first enter the basement?

with open('input.txt', 'r') as f:
    text = f.readlines()

floor = 0
position = 0

for lines in text:
    for character in lines:

        position += 1

        # Go up one floor
        if character == '(':
            floor += 1

        # Go down one floor
        elif character == ')':
            floor -= 1

        # First time entered basement
        if floor == -1:
            break

print(position)
