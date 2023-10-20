days = int(input())
room = input()
rate = input()
price = 0

nights = days - 1

if room == "room for one person":
    price = 18
elif room == "apartment":
    price = 25
elif room == "president apartment":
    price = 35

price = price * nights

discount = 0
if days < 10 and room == "apartment":
    discount = 0.3
    discount = price * discount
elif 10 <= days <= 15 and room == "apartment":
    discount = 0.35
    discount = price * discount
elif days > 15 and room == "apartment":
    discount = 0.5
    discount = price * discount
elif days < 10 and room == "president apartment":
    discount = 0.1
    discount = price * discount
elif 10 <= days <= 15 and room == "president apartment":
    discount = 0.15
    discount = price * discount
elif days > 15 and room == "president apartment":
    discount = 0.2
    discount = price * discount

first_price = price - discount

extra_discount = 0
if rate == "positive":
    extra_discount = first_price * 0.25
    final_price = first_price + extra_discount
elif rate == "negative":
    extra_discount = first_price * 0.1
    final_price = first_price - extra_discount

print(f"{final_price:.2f}")

