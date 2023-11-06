level = int(input())
rooms = int(input())
current_level = ""

for current_floor in range(level, 0, -1):
    if current_floor == level:
        current_level = "L"
    elif current_floor % 2 == 0:
        current_level = "O"
    else:
        current_level = "A"
    for current_room in range(rooms):
        print(f"{current_level}{current_floor}{current_room}", end=" ")
    print()
