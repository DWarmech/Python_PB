actor = input()
academy_points = float(input())
raters = int(input())
total_points = 0

points_sum = academy_points

for i in range(raters):
    rater = input()
    points = float(input())

    characters = len(rater)
    points_sum = points_sum + ((characters * points) / 2)
    total_points = points_sum

    if total_points > 1250.5:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points < 1250.5:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor} you need {needed_points:.1f} more!")
