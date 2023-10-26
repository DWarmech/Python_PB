budget = float(input())
category = input()
people = int(input())
transport = 0
ticket_price = 0

if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
elif people >= 50:
    transport = budget * 0.25

money_left = budget - transport

if category == "Normal":
    ticket_price = 249.99
elif category == "VIP":
    ticket_price = 499.99

ticket_price = ticket_price * people

if money_left >= ticket_price:
    money_left -= ticket_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    needed_money = ticket_price - money_left
    print(f"Not enough money! You need {needed_money:.2f} leva.")
