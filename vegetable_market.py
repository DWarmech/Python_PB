vegetable_kg_price = float(input())
fruit_kg_price = float(input())
vegetable_total = int(input())
fruit_total = int(input())

vegetable_price = vegetable_kg_price * vegetable_total
fruit_price = fruit_kg_price * fruit_total

total = vegetable_price + fruit_price
total_eur = total / 1.94

print("%.2f" % total_eur)
