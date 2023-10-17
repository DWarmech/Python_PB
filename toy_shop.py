excursion = float(input())
puzzles = int(input())
dolls = int(input())
teddies = int(input())
minions = int(input())
trucks = int(input())
discount = 0

total_sum = puzzles * 2.60 + dolls * 3 + teddies * 4.1 + minions * 8.2 + trucks * 2

toys_count = puzzles + dolls + teddies + minions + trucks

if toys_count >= 50:
    discount = total_sum * 0.25

final_sum = total_sum - discount

rent = final_sum * 0.1

profit = final_sum - rent

if profit >= excursion:
    for_excursion = profit - excursion
    print(f"Yes! {for_excursion:.2f} lv left.")
else:
    needed_excursion = excursion - profit
    print(f"Not enough money! {needed_excursion:.2f} lv needed.")
