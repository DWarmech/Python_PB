country = input()

while country != "End":
    budget = float(input())
    total = 0

    while total < budget:
        salary = float(input())
        total += salary
    print(f"Going to {country}!")

    country = input()
