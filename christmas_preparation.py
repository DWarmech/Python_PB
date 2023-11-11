rolling_paper = int(input())
material = int(input())
liters = float(input())
percent = int(input())

papers_price = rolling_paper * 5.8
material_price = material * 7.2
liters_price = liters * 1.2

all_price = papers_price + material_price + liters_price

discount = percent / 100

final_discount = all_price * discount

final_price = all_price - final_discount

print(f"{final_price:.3f}")
