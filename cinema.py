screen_type = input()
rows = int(input())
columns = int(input())
income = 0

capacity = rows * columns

if screen_type == "Premiere":
    income = capacity * 12
elif screen_type == "Normal":
    income = capacity * 7.5
elif screen_type == "Discount":
    income = capacity * 5

print(f"{income:.2f} leva")
