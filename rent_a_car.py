budget = float(input())
season = input()
car_type = ""
car = ""

if budget <= 100:
    car_type = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        car = "Jeep"
        car_price = budget * 0.65
elif 100 < budget <= 500:
    car_type = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        car = "Jeep"
        car_price = budget * 0.8
elif budget > 500:
    car_type = "Luxury class"
    car = "Jeep"
    car_price = budget * 0.9

print(car_type)
print(f"{car} - {car_price:.2f}")
