budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        used_money = budget * 0.3
        sleep = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{sleep} - {used_money:.2f}")
    elif season == "winter":
        used_money = budget * 0.7
        sleep = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{sleep} - {used_money:.2f}")
if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        used_money = budget * 0.4
        sleep = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{sleep} - {used_money:.2f}")
    elif season == "winter":
        used_money = budget * 0.8
        sleep = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{sleep} - {used_money:.2f}")
elif budget > 1000:
    destination = "Europe"
    used_money = budget * 0.9
    sleep = "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{sleep} - {used_money:.2f}")
