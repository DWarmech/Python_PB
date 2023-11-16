judges = int(input())
presentation = input()
counter = 0
total_grade = 0

while presentation != "Finish":
    final_grade = 0
    second_grade = 0

    for note in range(0, judges):
        counter += 1
        grade = float(input())

        total_grade += grade
        second_grade += grade

    final_grade = total_grade / judges
    second_grade = second_grade / judges

    print(f"{presentation} - {second_grade:.2f}.")

    presentation = input()

end_grade = total_grade / counter

print(f"Student's final assessment is {end_grade:.2f}.")
