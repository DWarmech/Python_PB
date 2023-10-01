trainings = int(input())

shoes = trainings - (trainings * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes * 0.25
accesories = ball * 0.2

total = trainings + shoes + clothes + ball + accesories

print(total)
