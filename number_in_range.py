city = input()
sales = float(input())
comissions = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        comissions = 0.05
    elif 500 <= sales <= 1000:
        comissions = 0.07
    elif 1000 <= sales <= 10000:
        comissions = 0.08
    elif 10000 <= sales:
        comissions = 0.12
elif city == "Varna":
    if 0 <= sales <= 500:
        comissions = 0.045
    elif 500 <= sales <= 1000:
        comissions = 0.075
    elif 1000 <= sales <= 10000:
        comissions = 0.1
    elif 10000 <= sales:
        comissions = 0.13
elif city == "Plovdiv":
    if 0 <= sales <= 500:
        comissions = 0.055
    elif 500 <= sales <= 1000:
        comissions = 0.08
    elif 1000 <= sales <= 10000:
        comissions = 0.12
    elif 10000 <= sales:
        comissions = 0.145

if comissions > 0:
    final_sum = sales * comissions
    print(f"{final_sum:.2f}")
else:
    print("error")
