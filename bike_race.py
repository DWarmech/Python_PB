juniors = int(input())
seniors = int(input())
trace = input()

if trace == "trail":
    juniors_tax = 5.5
    seniors_tax = 7
elif trace == "cross-country":
    juniors_tax = 8
    seniors_tax = 9.5

    if seniors + juniors >= 50:
        discount_tax = juniors_tax * 0.25
        discount_senior_tax = seniors_tax * 0.25
        juniors_tax = juniors_tax - discount_tax
        seniors_tax = seniors_tax - discount_senior_tax

elif trace == "downhill":
    juniors_tax = 12.25
    seniors_tax = 13.75
elif trace == "road":
    juniors_tax = 20
    seniors_tax = 21.5

total_sum = juniors * juniors_tax + seniors_tax * seniors
expenses = total_sum * 0.05
final = total_sum - expenses

print(f"{final:.2f}")
