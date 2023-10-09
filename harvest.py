import math

sq_m = int(input())
grapes_per_square_m = float(input())
needed_liters = int(input())
workers = int(input())

total_grapes = sq_m * grapes_per_square_m
wine = total_grapes * 0.4 / 2.5

if wine >= needed_liters:
    liters_left = wine - needed_liters
    liters_per_person = liters_left / workers
    wine = math.floor(wine)
    print(f"Good harvest this year! Total wine: {wine} liters.")
    liters_left = math.ceil(liters_left)
    liters_per_person = math.ceil(liters_per_person)
    print(f"{liters_left} liters left -> {liters_per_person} liters per person.")
elif wine < needed_liters:
    needed_liters = needed_liters - wine
    needed_liters = math.floor(needed_liters)
    print(f"It will be a tough winter! More {needed_liters} liters wine needed.")
