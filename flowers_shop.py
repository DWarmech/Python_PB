chrysa = int(input())
roses = int(input())
tulips = int(input())
season = input()
festive = input()

total_flowers = chrysa + roses + tulips

if season == "Spring" or season == "Summer":
    chrysa_unit = 2
    rose_unit = 4.1
    tulips_unit = 2.5
elif season == "Autumn" or season == "Winter":
    chrysa_unit = 3.75
    rose_unit = 4.5
    tulips_unit = 4.15

price = chrysa * chrysa_unit + roses * rose_unit + tulips_unit * tulips

if festive == "Y":
    festive_add = price * 0.15
    price += festive_add

if tulips >= 7 and season == "Spring":
    discount = price * 0.05
    price -= discount

if roses >= 10 and season == "Winter":
    discount = price * 0.1
    price -= discount

if total_flowers >= 20:
    discount = price * 0.2
    price -= discount

total_price = price + 2

print(f"{total_price:.2f}")

