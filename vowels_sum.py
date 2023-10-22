text = input()
char_sum = 0

for character in text:
    if character == "a":
        char_sum += 1
    elif character == "e":
        char_sum += 2
    elif character == "i":
        char_sum += 3
    elif character == "o":
        char_sum += 4
    elif character == "u":
        char_sum += 5

print(char_sum)
