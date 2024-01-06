# This year, how many houses receive at least one present?

class santa():
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0

with open('input.txt', 'r') as f:
    text = f.readlines()

# Start by counting the starting house
house = set()
house.add((0,0))

human_santa = santa()
robo_santa = santa()

people = [human_santa, robo_santa]
turn = 0 # to determine which santa is going

for character in text[0]:
    people[turn%2]

    if character == '^':
        people[turn%2].vertical += 1
    elif character == 'v':
        people[turn%2].vertical -= 1
    elif character == '<':
        people[turn%2].horizontal -= 1
    elif character == '>':
        people[turn%2].horizontal += 1

    coordinates = (people[turn%2].horizontal, people[turn%2].vertical)
    house.add(coordinates)
    turn += 1

print(len(house))