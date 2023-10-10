import math

days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

needed_dog = days * dog_food
needed_cat = days * cat_food
needed_turtle = days * turtle_food / 1000

total_food = needed_turtle + needed_cat + needed_dog

if total_food <= food:
    final_food = food - total_food
    final_food = math.floor(final_food)
    print(f"{final_food} kilos of food left.")
elif total_food > food:
    final_food = total_food - food
    final_food = math.ceil(final_food)
    print(f"{final_food} more kilos of food are needed.")
