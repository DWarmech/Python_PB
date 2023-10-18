budget = int(input())
season = input()
fishers = int(input())

if season == "Spring":
    boat_price = 3000
elif season == "Summer" or season == "Autumn":
    boat_price = 4200
else:
    boat_price = 2600

if fishers <= 6:
    discount = 0.1
elif 7 <= fishers <= 11:
    discount = 0.15
else:
    discount = 0.25

extra_discount = 0

if fishers % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

first_discount = boat_price * discount
total_sum = boat_price - first_discount
final_sum = total_sum - extra_discount

if budget >= final_sum:
    left_sum = budget - final_sum
    print(f"Yes! You have {left_sum:.2f} leva left.")
elif budget < final_sum:
    needed_sum = final_sum - budget
    print(f"Not enough money! You need {needed_sum:.2f} leva.")
