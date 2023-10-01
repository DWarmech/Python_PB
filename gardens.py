sqMeter = float(input())

price = sqMeter * 7.61
discount = 0.18 * price
total = price - discount

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")
