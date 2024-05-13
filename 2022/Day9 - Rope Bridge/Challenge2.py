# Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?

def update_tail(x_pos, y_pos, positions_visited):

    # Iterate through all the ten knots
    for i in range(0,9):

        if y_pos[i] == y_pos[i+1]:
            if abs(x_pos[i] - x_pos[i+1]) == 2:
                # if tail on left pos
                if x_pos[i+1] < x_pos[i]:
                    x_pos[i+1] += 1
                # if tail on right pos
                elif x_pos[i+1] > x_pos[i]:
                    x_pos[i+1] -= 1

        elif x_pos[i] == x_pos[i+1]:
            if abs(y_pos[i] - y_pos[i+1]) == 2:
                # if tail on top pos
                if y_pos[i+1] < y_pos[i]:
                    y_pos[i+1] += 1
                # if tail on bottom pos
                elif y_pos[i+1] > y_pos[i]:
                    y_pos[i+1] -= 1

        elif abs(x_pos[i] - x_pos[i+1]) == 2 or abs(y_pos[i] - y_pos[i+1]) == 2:
            # if tail on bottom left pos
            if y_pos[i+1] < y_pos[i] and x_pos[i+1] < x_pos[i]:
                y_pos[i+1] += 1
                x_pos[i+1] += 1
            # if tail on bottom right pos
            elif y_pos[i+1] < y_pos[i] and x_pos[i+1] > x_pos[i]:
                y_pos[i+1] += 1
                x_pos[i+1] -= 1
            # if tail on top left pos
            elif y_pos[i+1] > y_pos[i] and x_pos[i+1] < x_pos[i]:
                y_pos[i+1] -= 1
                x_pos[i+1] += 1
            # if tail on top right pos
            elif y_pos[i+1] > y_pos[i] and x_pos[i+1] > x_pos[i]:
                y_pos[i+1] -= 1
                x_pos[i+1] -= 1

    positions_visited.add((x_pos[9],y_pos[9]))
    return x_pos, y_pos

# Reading the file
with open('input.txt', 'r') as f:
    text = f.readlines()

positions_visited = set()

# The first index (x_pos[0]) will be head and last index(x_pos[9]) will be tail
x_pos = [0] * 10
y_pos = [0] * 10

positions_visited.add((x_pos[9],y_pos[9])) # Starting position

for instruction in text:

    direction, steps = instruction.split()

    for _ in range(int(steps)):
        if direction == 'R':
            x_pos[0] += 1
        elif direction == 'L':
            x_pos[0] -= 1
        elif direction == 'U':
            y_pos[0] += 1
        elif direction == 'D':
            y_pos[0] -= 1

        x_pos, y_pos = update_tail(x_pos, y_pos, positions_visited)

print(len(positions_visited))