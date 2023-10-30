name = input()
year = 1
is_expelled = False
grade = 0
bad_year = 0

while year <= 12:
    current_grade = float(input())

    if current_grade < 4:
        bad_year += 1
        if bad_year > 1:
            is_expelled = True
            break
        continue

    year += 1
    grade += current_grade

if is_expelled:
    print(f"{name} has been excluded at {year} grade")
else:
    average = grade / 12
    print(f"{name} graduated. Average grade: {average:.2f}")
