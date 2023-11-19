import math

paint = int(input())
wallpapers = int(input())
gloves_price = float(input())
brush_price = float(input())

paint_total = paint * 21.5
wallpapers_total = wallpapers * 5.2
needed_gloves = wallpapers * 0.35
needed_gloves = math.ceil(needed_gloves)
needed_brushes = paint * 0.48
needed_brushes = math.floor(needed_brushes)

gloves_total = needed_gloves * gloves_price
brushes_total = needed_brushes * brush_price

total_price = paint_total + wallpapers_total + gloves_total + brushes_total
delivery_price = total_price * 0.06666666667

print(f"This delivery will cost {delivery_price:.2f} lv.")
