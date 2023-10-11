fuel = str(input())
quantity = int(input())

if fuel == "Diesel":
    if quantity >= 25:
        print(f"You have enough diesel.")
    elif quantity < 25:
        print(f"Fill your tank with diesel!")
elif fuel == "Gas":
    if quantity >= 25:
        print(f"You have enough gas.")
    elif quantity < 25:
        print(f"Fill your tank with gas!")
elif fuel == "Gasoline":
    if quantity >= 25:
        print(f"You have enough gasoline.")
    elif quantity < 25:
        print(f"Fill your tank with gasoline!")
else:
    print("Invalid fuel!")
