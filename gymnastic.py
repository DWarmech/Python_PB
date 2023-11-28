country = input()
equipment = input()
x1 = 0
x2 = 0

if country == "Russia":
    if equipment == "ribbon":
        x1 = 9.100
        x2 = 9.400
    elif equipment == "hoop":
        x1 = 9.300
        x2 = 9.800
    elif equipment == "rope":
        x1 = 9.600
        x2 = 9.000
elif country == "Bulgaria":
    if equipment == "ribbon":
        x1 = 9.600
        x2 = 9.400
    elif equipment == "hoop":
        x1 = 9.550
        x2 = 9.750
    elif equipment == "rope":
        x1 = 9.500
        x2 = 9.400
elif country == "Italy":
    if equipment == "ribbon":
        x1 = 9.200
        x2 = 9.500
    elif equipment == "hoop":
        x1 = 9.450
        x2 = 9.350
    elif equipment == "rope":
        x1 = 9.700
        x2 = 9.150

final_score = x1 + x2
percent = 20 - final_score
percent = (percent / 20) * 100

print(f"The team of {country} get {final_score:.3f} on {equipment}.")
print(f"{percent:.2f}%")
