import math

record = float(input())
distance_m = float(input())
time = float(input())

distance_s = distance_m * time
water = distance_m / 15
water = math.floor(water)
seconds = water * 12.5

total_time = distance_s + seconds

if record <= total_time:
    needed_time = total_time - record
    print(f"No, he failed! He was {needed_time:.2f} seconds slower.")
elif record > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
