n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, 2 * n):
    number = int(input())
    if i < n:
        left_sum += number
    else:
        right_sum += number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = 0
    if left_sum > right_sum:
        difference = left_sum - right_sum
    else:
        difference = right_sum - left_sum

    print(f"No, diff = {difference}")
