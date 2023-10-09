km = int(input())
time = str(input())

if km < 20:  # Taxi
    if time == "day":
        price = 0.7 + (km * 0.79)
        print(f"{price:.2f}")
    elif time == "night":
        price = 0.7 + (km * 0.9)
        print(f"{price:.2f}")
elif 20 <= km < 100:  # Bus
    price = km * 0.09
    print(f"{price:.2f}")
elif km >= 100:  # Train
    price = km * 0.06
    print(f"{price:.2f}")
