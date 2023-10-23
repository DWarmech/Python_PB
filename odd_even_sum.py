n = int(input())
num = 0
even_total = 0
odd_total = 0

for number in range(0, n):
    num = int(input())

    if number % 2 == 0:
        even_total = num + even_total
    else:
        odd_total = num + odd_total

if even_total == odd_total:
    print("Yes")
    print(f"Sum = {even_total}")
else:
    difference = 0
    if even_total > odd_total:
        difference = even_total - odd_total
    elif odd_total > even_total:
        difference = odd_total - even_total
    print("No")
    print(f"Diff = {difference}")
