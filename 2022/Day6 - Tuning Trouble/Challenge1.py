# How many characters need to be processed before the first start-of-packet marker is detected?

with open('input.txt', 'r') as f:
    text = f.readlines()

LIMIT = 4
counter = 0
subroutine = ''
found_subroutine = False

for letter in text[0]:
    if len(subroutine) == LIMIT:
        for i in range(LIMIT):
            found_subroutine = True
            character = subroutine[i]

            # Slicing to remove character by index
            leftovers = subroutine[:i] + subroutine[i+1:]

            if character in leftovers:
                found_subroutine = False
                break
        # If there is a repeated character just go to the next letter
        if not found_subroutine:
            subroutine = subroutine[1:]

    if found_subroutine:
        break

    counter += 1
    subroutine += letter
    
print(counter)