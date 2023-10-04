mackerel_price = float(input())
tsatsa_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
mussels_kg = int(input())

safrid_price = tsatsa_price + tsatsa_price * 0.8
safrid_total = safrid_kg * safrid_price

mussels_price = mussels_kg * 7.5

palamud_price = mackerel_price + mackerel_price * 0.6
palamud_total = palamud_kg * palamud_price

total = palamud_total + safrid_total + mussels_price

print("%.2f" % total)

