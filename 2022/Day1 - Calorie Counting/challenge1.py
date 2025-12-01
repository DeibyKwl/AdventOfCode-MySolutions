# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

cal_counter = 0
max_cal_counter = 0

with open('input.txt', 'r') as f:
    text = f.readlines()

    for line in text:
        # Reset values and find max calory value
        if line == '\n':
            if cal_counter >= max_cal_counter:
                max_cal_counter = cal_counter
            cal_counter = 0
        else:
            cal_counter += int(line)

print(max_cal_counter)
