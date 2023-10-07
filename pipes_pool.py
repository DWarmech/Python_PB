size = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_total = p1 * h
p2_total = p2 * h
p_total = p1_total + p2_total

if size >= p_total:
    percent_full = (p_total / size) * 100
    p1_percent = (p1_total / p_total) * 100
    p2_percent = (p2_total / p_total) * 100
    print(f"The pool is {percent_full:.2f}% full.\
 Pipe 1: {p1_percent:.2f}%. Pipe 2: {p2_percent:.2f}%.")

elif size < p_total:
    overflow = p_total - size
    print(f"For {h:.2f} hours the pool overflows with {overflow:.2f} liters.")
