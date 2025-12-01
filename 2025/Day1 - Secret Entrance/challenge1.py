# Analyze the rotations in your attached document. What's the actual password to open the door?

zero_counter = 0
dial_pos = 50

with open('input.txt', 'r') as f:
    text = f.readlines()

    for line in text:
        # Clean the line
        rotation = line.strip()

        # Left rotation
        if rotation[0] == 'L':
            dial_pos -= int(rotation[1::1])
            # Normalize the number to (0-99)
            while dial_pos <= -1:
                dial_pos = 100 + dial_pos

        # Right rotation
        elif rotation[0] == 'R':
            dial_pos += int(rotation[1::1])
            # Normalize the number to (0-99)
            while dial_pos >= 100:
                dial_pos = dial_pos - 100
        
        # Add to the counter if dial is at zero
        if dial_pos == 0:
            zero_counter += 1

print(zero_counter)