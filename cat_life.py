import math

cat_type = input()
gender = input()
years = 0

if cat_type == "British Shorthair":
    if gender == "m":
        years = 13
    elif gender == "f":
        years = 14
elif cat_type == "Siamese":
    if gender == "m":
        years = 15
    elif gender == "f":
        years = 16
elif cat_type == "Persian":
    if gender == "m":
        years = 14
    elif gender == "f":
        years = 15
elif cat_type == "Ragdoll":
    if gender == "m":
        years = 16
    elif gender == "f":
        years = 17
elif cat_type == "American Shorthair":
    if gender == "m":
        years = 12
    elif gender == "f":
        years = 13
elif cat_type == "Siberian":
    if gender == "m":
        years = 11
    elif gender == "f":
        years = 12

if years == 0:
    print(f"{cat_type} is invalid cat!")
elif years != 0:
    human_months = years * 12
    cat_months = human_months / 6

    print(f"{math.trunc(cat_months)} cat months")
