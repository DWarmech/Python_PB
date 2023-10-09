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
    final_sum = total_sum * 0.15

    print(f"Youhave{остатъченбюджет} levaleft!")
