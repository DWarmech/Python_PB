days = int(input())
total_quantity = 0
degrees_total = 0

for days in range(0, days, 1):
    quantity = float(input())
    degrees = float(input())

    total_quantity += quantity
    degrees_total += quantity * degrees

average = degrees_total / total_quantity

print(f"Liter: {total_quantity:.2f}")
print(f"Degrees: {average:.2f}")

if average < 38:
    print("Not good, you should baking!")
elif 38 <= average <= 42:
    print("Super!")
elif average > 42:
    print("Dilution with distilled water!")
