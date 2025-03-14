numbers = []

for i in range(1, 11):
    num = int(input(f"Enter a number({i} of 10): "))
    numbers += [num]

print("\nThe unique numbers are:")

for num in numbers:
    if numbers.count(num) == 1:
        print(num)