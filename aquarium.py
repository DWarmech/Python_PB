size = int(input())
width = int(input())
height = int(input())
percent = float(input())

obem = size * width * height
obem_Liters = obem * 0.001
taken = percent * 0.01
needed_Liters = obem_Liters * (1 - taken)

print(needed_Liters)

