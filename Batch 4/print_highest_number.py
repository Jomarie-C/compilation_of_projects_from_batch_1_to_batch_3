numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

highest_num = 0

for num in numbers:
    if num > highest_num:
        highest_num = num