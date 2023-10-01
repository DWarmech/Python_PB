pages = int(input())
pagesPerHour = int(input())
days = int(input())

timePerBook = pages / pagesPerHour
hoursPerDay = timePerBook / days

print(int(hoursPerDay))
