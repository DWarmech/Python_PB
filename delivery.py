chicken = int(input())
fish = int(input())
vegan = float(input())

chickenPrice = chicken * 10.35
fishPrice = fish * 12.4
veganPrice = vegan * 8.15  # Too many decimals

menu = chickenPrice + fishPrice + veganPrice

dessert = menu * 0.2
delivery = 2.5

deliveryPrice = menu + dessert + delivery

rounded = round(deliveryPrice, 2)

print(rounded)



