numbers = []

for i in range(1, 11):
    num = int(input(f"Enter a number({i} of 10): "))
    if num not in numbers:
        numbers.append(num)