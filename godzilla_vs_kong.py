import math

budget = float(input())
statists = int(input())
clothes_per_statist = float(input())
discount = 0

decor = budget * 0.1
clothes_sum = statists * clothes_per_statist

if statists > 150:
    discount = clothes_sum * 0.1
    clothes_sum = clothes_sum - discount

movie_sum = decor + clothes_sum

if movie_sum <= budget:
    final_sum = budget - movie_sum
    final_sum = abs(final_sum)
    print("Action!")
    print(f"Wingard starts filming with {final_sum:.2f} leva left.")
elif movie_sum > budget:
    final_sum = budget - movie_sum
    final_sum = abs(final_sum)
    print("Not enough money!")
    print(f"Wingard needs {final_sum:.2f} leva more.")
