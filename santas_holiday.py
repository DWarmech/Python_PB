days = int(input())
room_type = input()
feedback = input()
price = 0
discount = 0

stayed_nights = days - 1

if room_type == "room for one person":
    price = 18
elif room_type == "apartment":
    price = 25
elif room_type == "president apartment":
    price = 35

stay_price = stayed_nights * price

if days < 10:
    if room_type == "apartment":
        discount = 0.3
    elif room_type == "president apartment":
        discount = 0.1
elif 10 <= days < 15:
    if room_type == "apartment":
        discount = 0.35
    elif room_type == "president apartment":
        discount = 0.15
elif days > 15:
    if room_type == "apartment":
        discount = 0.5
    elif room_type == "president apartment":
        discount = 0.20

discount = stay_price * discount
discount_stay = stay_price - discount

if feedback == "positive":
    feedback_discount = discount_stay * 0.25
    final_price = discount_stay + feedback_discount
elif feedback == "negative":
    feedback_discount = discount_stay * 0.1
    final_price = discount_stay - feedback_discount

print(f"{final_price:.2f}")
