import math

tournaments = int(input())
starting_points = int(input())
total_points = 0
additional_points = 0
p1 = 0
p2 = 0
p3 = 0

add_points = starting_points

for i in range(tournaments):
    position = input()

    if position == "W":
        additional_points = 2000
        p1 += 1
    elif position == "F":
        additional_points = 1200
        p2 += 1
    elif position == "SF":
        additional_points = 720
        p3 += 1

    add_points = add_points + additional_points

average_points = ((p1 * 2000) + (p2 * 1200) + (p3 * 720)) / tournaments

won_tournaments = (p1 / tournaments) * 100

print(f"Final points: {add_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{won_tournaments:.2f}%")

