cats = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
total_food = 0

for cat in range(0, cats):
    food_quantity = float(input())
    if 100 <= food_quantity < 200:
        group_1 += 1
    elif 200 <= food_quantity < 300:
        group_2 += 1
    elif 300 <= food_quantity < 400:
        group_3 += 1

    total_food = total_food + food_quantity

food_price = total_food / 1000
food_price = food_price * 12.45

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {food_price:.2f} lv.")
