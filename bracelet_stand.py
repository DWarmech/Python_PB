daily_money = float(input())
daily_profit = float(input())
expenses = float(input())
price = float(input())

saved = daily_money * 5
earned = daily_profit * 5
total_saved = saved + earned
after_expenses = total_saved - expenses

if after_expenses >= price:
    print(f"Profit: {after_expenses:.2f} BGN, the gift has been purchased.")
elif after_expenses < price:
    needed = price - after_expenses
    print(f"Insufficient money: {needed:.2f} BGN.")
