locations = int(input())

for location in range(0, locations):
    daily_expected = int(input())
    dig_days = int(input())
    average = 0

    for kg in range(0, dig_days):
        dig = int(input())
        average = average + dig
    average_dig = average / dig_days

    if average_dig >= daily_expected:
        print(f"Good job! Average gold per day: {average_dig:.2f}.")

    elif average_dig < daily_expected:
        daily_expected -= average_dig
        print(f"You need {daily_expected:.2f} gold.")
