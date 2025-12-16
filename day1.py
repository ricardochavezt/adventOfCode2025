import fileinput
import sys

def debug_print(*args):
    if "--debug" in sys.argv:
        print(*args)

dial_pos = 50
debug_print("The dial starts at", dial_pos)
password = 0
for line in fileinput.input('-'):
    direction, distance = line[0], int(line[1:])
    if direction == "R":
        next_pos = (dial_pos + distance)
    else:
        next_pos = (dial_pos - distance)
    next_pos = next_pos % 100
    password += (1 if next_pos == 0 else 0)
    debug_print("The dial is rotated", line.strip(), "to point at", next_pos)
    if "--part2" in sys.argv:
        full_rotations, remainder = divmod(distance, 100)
        debug_print("Full rotations:", full_rotations)
        password += full_rotations
        if next_pos != 0 and remainder > 0:
            if direction == "R" and (dial_pos + remainder) > 99:
                debug_print("Passed 0")
                password += 1
            elif direction == "L" and dial_pos > 0 and (dial_pos - remainder) < 0:
                debug_print("Passed 0")
                password += 1

    dial_pos = next_pos

print("Password:", password)