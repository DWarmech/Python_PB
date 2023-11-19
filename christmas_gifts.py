command = input()
underage = 0
older = 0

while command != "Christmas":
    age = int(command)

    if age <= 16:
        underage += 1
    elif age > 16:
        older += 1

    command = input()

toys_price = underage * 5
sweater_price = older * 15

print(f"Number of adults: {older}")
print(f"Number of kids: {underage}")
print(f"Money for toys: {toys_price}")
print(f"Money for sweaters: {sweater_price}")
