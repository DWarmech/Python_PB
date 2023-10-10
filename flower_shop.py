import math

magnolias = int(input())
hyacinths = int(input())
roses = int(input())
cacti = int(input())
gift_price = float(input())

price = magnolias * 3.25 + hyacinths * 4 + roses * 3.5 + cacti * 8
taxes = price * 0.05
profit = price - taxes

if profit < gift_price:
    final_sum = gift_price - profit
    final_sum = math.ceil(final_sum)
    print(f"She will have to borrow {final_sum} leva.")
elif profit >= gift_price:
    final_sum = profit - gift_price
    final_sum = math.floor(final_sum)
    print(f"She is left with {final_sum} leva.")
