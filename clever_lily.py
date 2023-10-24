age = int(input())
machine_price = float(input())
toy = int(input())
birthday_saved = 0
birthday_money = 0
toys = 0
brother = 0

for years in range(1, age + 1):

    if years % 2 == 0:
        birthday_money += 10
        birthday_saved = birthday_money + birthday_saved
        brother += 1
    else:
        toys += 1

toys_saved = toys * toy

saved_money = birthday_saved + toys_saved
total_money = saved_money - brother

if total_money >= machine_price:
    left_money = total_money - machine_price
    print(f"Yes! {left_money:.2f}")
else:
    needed_money = machine_price - total_money
    print(f"No! {needed_money:.2f}")
