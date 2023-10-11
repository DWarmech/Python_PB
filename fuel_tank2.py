fuel = str(input())
quantity = float(input())
card = str(input())
discount = 0

if fuel == "Gas":
    price = 0.93
    if card == "Yes":
        price = price - 0.08
    total_price = quantity * price
    if 20 < quantity <= 25:
        discount = total_price * 0.08
    elif quantity > 25:
        discount = total_price * 0.1
    total_price = total_price - discount
    print(f"{total_price:.2f} lv.")

elif fuel == "Gasoline":
    price = 2.22
    if card == "Yes":
        price = price - 0.18
    total_price = quantity * price
    if 20 < quantity <= 25:
        discount = total_price * 0.08
    elif quantity > 25:
        discount = total_price * 0.1
    total_price = total_price - discount
    print(f"{total_price:.2f} lv.")

elif fuel == "Diesel":
    price = 2.33
    if card == "Yes":
        price = price - 0.12
    total_price = quantity * price
    if 20 < quantity <= 25:
        discount = total_price * 0.08
    elif quantity > 25:
        discount = total_price * 0.1
    total_price = total_price - discount
    print(f"{total_price:.2f} lv.")
