groups = int(input())
total_people = 0
climbers1 = 0
climbers2 = 0
climbers3 = 0
climbers4 = 0
climbers5 = 0

for i in range(groups):
    per_group = int(input())

    total_people = total_people + per_group

    if per_group < 6:
        climbers1 = climbers1 + per_group
    elif 6 <= per_group < 13:
        climbers2 = climbers2 + per_group
    elif 13 <= per_group < 26:
        climbers3 = climbers3 + per_group
    elif 26 <= per_group < 41:
        climbers4 = climbers4 + per_group
    else:
        climbers5 = climbers5 + per_group

musala_climbers = climbers1 / total_people * 100
monblan_climbers = climbers2 / total_people * 100
killimandjaro_climbers = climbers3 / total_people * 100
k2_climbers = climbers4 / total_people * 100
everest_climbers = climbers5 / total_people * 100

print(f"{musala_climbers:.2f}%")
print(f"{monblan_climbers:.2f}%")
print(f"{killimandjaro_climbers:.2f}%")
print(f"{k2_climbers:.2f}%")
print(f"{everest_climbers:.2f}%")
