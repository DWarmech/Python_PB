width = int(input())
length = int(input())
height = int(input())
free_space = 0
total_sq_meters = 0
sq_meters_met = False

available_space = width * length * height

command = input()
while command != "Done":
    sq_meters = int(command)

    total_sq_meters = total_sq_meters + sq_meters

    if total_sq_meters >= available_space:
        break

    command = input()

final_space = available_space - total_sq_meters

if final_space <= 0:
    print(f"No more free space! You need {abs(final_space)} Cubic meters more.")
else:
    print(f"{final_space} Cubic meters left.")
