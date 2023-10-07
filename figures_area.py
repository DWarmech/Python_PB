import math

shape = str(input())

if shape == "square":
    size1 = float(input())
    size = size1 * size1
    print(f"{size:.3f}")
elif shape == "rectangle":
    size1 = float(input())
    size2 = float(input())
    area = size1 * size2
    print(f"{area:.3f}")
elif shape == "circle":
    size1 = float(input())
    area = math.pi * (size1 * size1)
    print(f"{area:.3f}")
elif shape == "triangle":
    size1 = float(input())
    size2 = float(input())
    area = size1 * size2 / 2
    print(f"{area:.3f}")
