# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

cal_counter = 0
max_cal_counter = 0
top_three = [0,0,0]

with open('input.txt', 'r') as f:
    text = f.readlines()

    for line in text:
        #Reset value and add the new maximum calorie value to top three list
        if line == '\n':
            if cal_counter >= min(top_three):
                top_three[top_three.index(min(top_three))] = cal_counter
            cal_counter = 0
        else:
            cal_counter += int(line)

print(sum(top_three))

