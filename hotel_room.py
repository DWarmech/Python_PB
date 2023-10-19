month = input()
nights = int(input())

if month == "May" or month == "October":
    studio_night = 50
    apartment_night = 65

    studio_discount = 0
    if 7 < nights <= 14:
        discount = 0.05
        studio_discount = studio_night * discount
    elif nights > 14:
        discount = 0.3
        studio_discount = studio_night * discount

    apartment_discount = 0
    if nights > 14:
        discount = 0.1
        apartment_discount = apartment_night * discount

    apartment_price = (nights * apartment_night) - (apartment_discount * nights)
    print(f"Apartment: {apartment_price:.2f} lv.")
    studio_price = (nights * studio_night) - (studio_discount * nights)
    print(f"Studio: {studio_price:.2f} lv.")

elif month == "June" or month == "September":
    studio_night = 75.2
    apartment_night = 68.7

    studio_discount = 0
    if nights > 14:
        discount = 0.2
        studio_discount = studio_night * discount

    apartment_discount = 0
    if nights > 14:
        discount = 0.1
        apartment_discount = apartment_night * discount

    apartment_price = (nights * apartment_night) - (apartment_discount * nights)
    print(f"Apartment: {apartment_price:.2f} lv.")
    studio_price = (nights * studio_night) - (studio_discount * nights)
    print(f"Studio: {studio_price:.2f} lv.")

elif month == "July" or month == "August":
    studio_night = 76
    apartment_night = 77

    apartment_discount = 0
    if nights > 14:
        discount = 0.1
        apartment_discount = apartment_night * discount

    apartment_price = (nights * apartment_night) - (apartment_discount * nights)
    print(f"Apartment: {apartment_price:.2f} lv.")
    studio_price = (nights * studio_night)
    print(f"Studio: {studio_price:.2f} lv.")
