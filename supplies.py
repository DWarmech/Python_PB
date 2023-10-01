pens = int(input())
markers = int(input())
bottle = int(input())
discount = int(input())

totalPens = pens * 5.8
totalMarkers = markers * 7.2
totalBottles = bottle * 1.2
total = totalPens + totalMarkers + totalBottles

totalDiscount = discount * 0.01
totalWDiscount = total - (total * totalDiscount)

print(totalWDiscount)
