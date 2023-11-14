command = input()
prime_nums = 0
not_prime_nums = 0

while command != "stop":
    number = int(command)

    if number < 0:
        print("Number is negative.")
        command = input()

    if number > 1 or number == 0:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                not_prime_nums += number
                command = input()
                break
        else:
            prime_nums += number
            command = input()

print(f"Sum of all prime numbers is: {prime_nums}")
print(f"Sum of all non prime numbers is: {not_prime_nums}")
