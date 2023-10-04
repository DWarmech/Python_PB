w = float(input())
h = float(input())

width = (h * 100) - 100
width_tables = width / 70
width_tables = int(width_tables)

length = w * 100
length_tables = length / 120
length_tables = int(length_tables)

desks = width_tables * length_tables - 3

print(desks)
