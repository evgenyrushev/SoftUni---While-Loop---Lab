import sys
number = input()

max = -10000000

while number != "Stop":
    num = int(number)

    if num > max:
        max = num
    number = input()

print(max)
