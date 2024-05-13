# Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

def update_tail(hx, hy, tx, ty, positions_visited):

    if hy == ty:
        if abs(hx- tx) == 2:
            # if tail on left pos
            if tx < hx:
                tx += 1
            # if tail on right pos
            elif tx > hx:
                tx -= 1

    elif hx == tx:
        if abs(hy - ty) == 2:
            # if tail on top pos
            if ty < hy:
                ty += 1
            # if tail on bottom pos
            elif ty > hy:
                ty -= 1

    elif abs(hx - tx) == 2 or abs(hy - ty) == 2:
            # if tail on bottom left pos
            if ty < hy and tx < hx:
                ty += 1
                tx += 1
            # if tail on bottom right pos
            elif ty < hy and tx > hx:
                ty += 1
                tx -= 1
            # if tail on top left pos
            elif ty > hy and tx < hx:
                ty -= 1
                tx += 1
            # if tail on top right pos
            elif ty > hy and tx > hx:
                ty -= 1
                tx -= 1

    positions_visited.add((tx,ty))
    return tx, ty # Update tails

# Reading the file
with open('input.txt', 'r') as f:
    text = f.readlines()

positions_visited = set()

hx, hy = 0,0
tx, ty = 0,0

positions_visited.add((tx,ty)) # Starting position

for instruction in text:

    direction, steps = instruction.split()

    for _ in range(int(steps)):
        if direction == 'R':
            hx += 1
        elif direction == 'L':
            hx -= 1
        elif direction == 'U':
            hy += 1
        elif direction == 'D':
            hy -= 1
        
        tx,ty = update_tail(hx,hy,tx,ty,positions_visited)

print(len(positions_visited))