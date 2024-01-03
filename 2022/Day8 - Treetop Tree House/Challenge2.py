# Consider each tree on your map. What is the highest scenic score possible for any tree?

with open('input.txt', 'r') as f:
    tree = f.readlines()

visible_counter = 0
column = 0
row = 0
highest_score = 0
selected_c = 0
selected_r = 0

for _ in tree:
    for tree_height in _:

        # Make sure not to count trees in the edges
        if not (column == 0 or column == len(tree) - 1) \
            and not (row == 0 or row == len(tree) - 1) \
                and tree_height.isdigit():
            
            scenic_score = 1
            tree_counter = 0

            # Compare to Upper tree(s)
            for i in range(1, column + 1):
                tree_counter += 1
                if int(tree[column][row]) <= int(tree[column - i][row]) or column - i == 0:
                    scenic_score *= tree_counter
                    tree_counter = 0
                    break

            # Compare to Bottom tree(s)
            for i in range(1, len(tree) - column):
                tree_counter += 1
                if int(tree[column][row]) <= int(tree[column + i][row]) or column + i == len(tree) - 1:
                    scenic_score *= tree_counter
                    tree_counter = 0
                    break

            # Compare to Left tree(s)
            for i in range(1, row + 1):
                tree_counter += 1
                if int(tree[column][row]) <= int(tree[column][row - i]) or row - i == 0:
                    scenic_score *= tree_counter
                    tree_counter = 0
                    break

            # Compare to right tree(s)
            for i in range(1, len(tree) - row):
                tree_counter += 1
                if int(tree[column][row]) <= int(tree[column][row + i]) or row + i == len(tree) - 1:
                    scenic_score *= tree_counter
                    tree_counter = 0
                    break

            # Find highes scenic score
            if scenic_score > highest_score:
                highest_score = scenic_score

        row += 1

    column += 1  # next line
    row = 0 # reset

print(highest_score)