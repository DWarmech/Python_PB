failed_threshold = int(input())
command = input()
exercises = 0
total_grade = 0
break_need = 0

while command != "Enough":
    exercise = command
    grade = int(input())
    exercises += 1

    if grade <= 4:
        break_need += 1
        if break_need >= failed_threshold:
            break

    total_grade += grade
    final_grade = total_grade / exercises

    command = input()
if command == "Enough":
    print(f"Average score: {final_grade:.2f}")
    print(f"Number of problems: {exercises}")
    print(f"Last problem: {exercise}")
else:
    print(f"You need a break, {break_need} poor grades.")
