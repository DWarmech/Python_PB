import math

racket_price = float(input())
racket_quantity = int(input())
shoes_quantity = int(input())

racket_total = racket_price * racket_quantity
per_shoe = racket_price / 6
shoes_total = shoes_quantity * per_shoe
left_equipment = (racket_total + shoes_total) * 0.2
total_price = left_equipment + shoes_total + racket_total
djokovich_sum = total_price / 8
sponsors_sum = total_price * 7 / 8

print(f"Price to be paid by Djokovic {math.floor(djokovich_sum)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_sum)}")
