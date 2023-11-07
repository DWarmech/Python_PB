import math

width = int(input())
length = int(input())
pieces_left = 0

pieces = width * length

command = input()
while not command == "STOP" and pieces_left >= 0:
    taken_piece = int(command)

    pieces = pieces - taken_piece

    if pieces <= 0:
        print(f"No more cake left! You need {abs(pieces)} pieces more.")
        break

    command = input()

if pieces > 0:
    print(f"{pieces} pieces are left.")



