import math

first = int(input())
second = int(input())
third = int(input())

total = first + second + third

total_minutes = total / 60
total_seconds = total % 60

total_minutes = math.floor(total_minutes)

if total_seconds < 10:
    print(f"{total_minutes}:0{total_seconds}")
else:
    print(f"{total_minutes}:{total_seconds}")
    
