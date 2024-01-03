# Consider your map; how many trees are visible from outside the grid?

with open('input.txt', 'r') as f:
    tree = f.readlines()

visible_counter = 0
column = 0
row = 0

for _ in tree:
    for tree_height in _:
        # Top and bottom of the grid
        if (column == 0 or column == len(tree) - 1) and tree_height.isdigit():
            visible_counter += 1
            
        # Edges of the grid
        elif (row == 0 or row == len(tree) - 1) and tree_height.isdigit():
            visible_counter += 1
            
        # Inner trees of the grid
        elif tree_height.isdigit():
            
            # To keep track if tree is covered
            covered = 0

            # Compare to Upper tree(s)
            for i in range(1, column + 1):
                if int(tree[column][row]) <= int(tree[column - i][row]):
                    covered += 1
                    break

            # # Compare to Bottom tree(s)
            for i in range(1, len(tree) - column):
                if int(tree[column][row]) <= int(tree[column + i][row]):
                    covered += 1
                    break

            # # Compare to Left tree(s)
            for i in range(1, row + 1):
                if int(tree[column][row]) <= int(tree[column][row - i]):
                    covered += 1
                    break

            # # Compare to right tree(s)
            for i in range(1, len(tree) - row):
                if int(tree[column][row]) <= int(tree[column][row + i]):
                    covered += 1
                    break

            # If tree covered in the 4 directions
            if covered < 4:
                visible_counter += 1

        row += 1

    column += 1  # next line
    row = 0 # reset

print(visible_counter)