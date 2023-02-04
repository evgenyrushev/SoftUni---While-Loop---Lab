number = input()

minimum = 10000000

while number != "Stop":
    num = int(number)

    if num < minimum:
        minimum = num
    number = input()

print(minimum)