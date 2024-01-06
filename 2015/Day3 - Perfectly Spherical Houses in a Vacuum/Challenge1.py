# How many houses receive at least one present?

with open('input.txt', 'r') as f:
    text = f.readlines()

horizontal = 0
vertical = 0

# Start by counting the starting house
house = set((0,0))

for character in text[0]:

    if character == '^':
        vertical += 1
    elif character == 'v':
        vertical -= 1
    elif character == '<':
        horizontal -= 1
    elif character == '>':
        horizontal += 1

    coordinates = (horizontal, vertical)
    house.add(coordinates)

print(len(house))