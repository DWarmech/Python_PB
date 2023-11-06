n1 = int(input())
n2 = int(input())
n3 = int(input())
combinations = 0
found_combination = False

for i in range(n1, n2 + 1):
    for m in range(n1, n2 + 1):
        combinations += 1
        if i + m == n3:
            found_combination = True
            break
    if found_combination:
        break


if found_combination:
    print(f"Combination N:{combinations} ({i} + {m} = {n3})")
else:
    print(f"{combinations} combinations - neither equals {n3}")
