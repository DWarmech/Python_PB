import math

rest_days = int(input())

work_days = 365 - rest_days
playtime_rest = 127 * rest_days
playtime_work = 63 * work_days

playtime = playtime_work + playtime_rest

if playtime < 30000:
    total_minutes = 30000 - playtime
    hours = total_minutes / 60
    minutes = total_minutes % 60
    print("Tom sleeps well")
    print(f"{math.floor(hours)} hours and {minutes} minutes less for play")
elif playtime > 30000:
    total_minutes = playtime - 30000
    hours = total_minutes / 60
    minutes = total_minutes % 60
    print("Tom will run away")
    print(f"{math.floor(hours)} hours and {minutes} minutes more for play")
