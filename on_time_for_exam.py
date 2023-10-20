test_hour = int(input())
test_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

test_hour_minutes = test_hour * 60 + test_minute
arrival_hour_minutes = arrival_hour * 60 + arrival_minute

diff = arrival_hour_minutes - test_hour_minutes

if diff > 0:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hh = diff // 60
        mm = diff % 60
        print(f"{hh}:{mm :02d} hours after the start")
elif diff >= -30:
    print("On time")
    if diff != 0:
        print(f"{abs(diff)} minutes before the start")
else:
    print("Early")
    if diff > -60:
        print(f"{abs(diff)} minutes before the start")
    else:
        hh = abs(diff) // 60
        mm = abs(diff) % 60
        print(f"{hh}:{mm :02d} hours before the start")
