k = int(input())
l = int(input())
m = int(input())
n = int(input())
x_change_possible = False
y_change_possible = False
x3 = 0
y3 = 0
changes = 0

for x1 in range(k, 9):
    for x2 in range(9, l - 1, -1):
        if x1 % 2 == 0 and x2 % 2 == 1:
            x_change_possible = True
        else:
            x_change_possible = False
        if x_change_possible:
            x3 = f"{x1}{x2}"
        for y1 in range(m, 9):
            for y2 in range(9, n - 1, -1):
                if changes == 6:
                    break
                if y1 % 2 == 0 and y2 % 2 == 1:
                    y_change_possible = True
                else:
                    y_change_possible = False
                if y_change_possible:
                    y3 = f"{y1}{y2}"
                    if x3 == y3 and x_change_possible and y_change_possible:
                        print("Cannot change the same player.")
                    elif x_change_possible and y_change_possible:
                        print(f"{x3} - {y3}")
                        changes += 1
