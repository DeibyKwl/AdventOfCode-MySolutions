# Using password method 0x434C49434B, what is the password to open the door?

zero_counter = 0
dial_pos = 50
zero_flag = True

with open('input.txt', 'r') as f:
    text = f.readlines()

    for line in text:
        # Clean the line
        rotation = line.strip()

        # Used for Left rotation (Avoid double counting)
        if dial_pos == 0:
            zero_flag = False
        
        # Left rotation
        if rotation[0] == 'L':
            dial_pos -= int(rotation[1::1])
            if dial_pos == 0:
                zero_counter += 1
            else:
                # Normalize the number to (0-99)
                while dial_pos <= -1:
                    dial_pos = 100 + dial_pos
                    # Flag to start counting if 0 was not the previous dial position
                    if zero_flag:
                        zero_counter += 1
                    zero_flag = True
                # Add one more in the case that dial point at 0 after several left rotations
                if dial_pos == 0:
                    zero_counter += 1
                    
        # Right rotation
        elif rotation[0] == 'R':
            dial_pos += int(rotation[1::1])
            zero_flag = True
            # Normalize the number to (0-99)
            while dial_pos >= 100:
                dial_pos = dial_pos - 100
                zero_counter += 1

print(zero_counter)