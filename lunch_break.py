import math

series = str(input())
episode = int(input())
rest = int(input())

lunch_time = rest * 0.125
rest_time = rest * 0.25
time_left = rest - lunch_time - rest_time

watch_time = time_left - episode

if time_left >= episode:
    watch_time = math.ceil(watch_time)
    print(f"You have enough time to watch {series} and left with {watch_time} minutes free time.")
elif time_left < episode:
    if watch_time < 0:
        watch_time = abs(watch_time)
    watch_time = math.ceil(watch_time)
    print(f"You don't have enough time to watch {series}, you need {watch_time} more minutes.")
