command = input()
counter = 1
climbed = 5364

while command != "END":
    new_meters = int(input())

    if command == "Yes":
        counter += 1
        if counter > 5:
            print("Failed!")
            print(f"{climbed}")
            break

    climbed += new_meters

    if climbed >= 8848:
        print(f"Goal reached for {counter} days!")
        break

    command = input()

if command == "END":
    print("Failed!")
    print(f"{climbed}")
