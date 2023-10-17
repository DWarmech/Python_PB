flower_type = input()
flowers = int(input())
budget = int(input())
price = 0
final_sum = 0

if flower_type == "Roses":
    price = flowers * 5
elif flower_type == "Dahlias":
    price = flowers * 3.8
elif flower_type == "Tulips":
    price = flowers * 2.8
elif flower_type == "Narcissus":
    price = flowers * 3
elif flower_type == "Gladiolus":
    price = flowers * 2.5

if flowers > 80 and flower_type == "Roses":
    discount = price * 0.1
    price = price - discount
elif flowers > 90 and flower_type == "Dahlias":
    discount = price * 0.15
    price = price - discount
elif flowers > 80 and flower_type == "Tulips":
    discount = price * 0.15
    price = price - discount
elif flowers < 120 and flower_type == "Narcissus":
    discount = price * 0.15
    price = price + discount
elif flowers < 80 and flower_type == "Gladiolus":
    discount = price * 0.2
    price = price + discount

if price <= budget:
    left_sum = budget - price
    print(f"Hey, you have a great garden with {flowers} {flower_type} and {left_sum:.2f} leva left.")
elif price > budget:
    needed_sum = price - budget
    print(f"Not enough money, you need {needed_sum:.2f} leva more.")
