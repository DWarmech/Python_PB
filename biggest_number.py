import sys

biggest_number = -sys.maxsize
command = input()

while command != "Stop":
    number = int(command)

    if number > biggest_number:
        biggest_number = number

    command = input()

print(biggest_number)

