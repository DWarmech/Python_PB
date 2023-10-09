budget = float(input())
gpu = int(input())
cpu = int(input())
ram = int(input())

gpu_sum = gpu * 250
cpu_price = gpu_sum * 0.35
cpu_sum = cpu * cpu_price
ram_price = gpu_sum * 0.1
ram_sum = ram_price * ram

total_sum = gpu_sum + cpu_sum + ram_sum

if gpu > cpu:
    discount = total_sum * 0.15
    total_sum = total_sum - discount

if budget >= total_sum:
    final_budget = budget - total_sum
    print(f"You have {final_budget:.2f} leva left!")
elif budget < total_sum:
    final_budget = total_sum - budget
    print(f"Not enough money! You need {final_budget:.2f} leva more!")

