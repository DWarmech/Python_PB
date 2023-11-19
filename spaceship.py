import math

width = float(input())
length = float(input())
height = float(input())
medium_astronaut_height = float(input())

rocket_size = width * length * height
single_room = (medium_astronaut_height + 0.4) * 2 * 2
astronauts = rocket_size / single_room
astronauts = math.floor(astronauts)

if 3 <= astronauts <= 10:
    print(f"The spacecraft holds {astronauts} astronauts.")
elif astronauts <= 3:
    print(f"The spacecraft is too small.")
elif astronauts >= 10:
    print(f"The spacecraft is too big.")
