numbers = []

for i in range(1, 11):
    num = int(input(f"Enter a number({i} of 10): "))
    numbers.append(num)

duplicates = set()
for num in numbers:
    if numbers.count(num) > 1:
        duplicates.add(num)

print("\nThe numbers that have duplicates are", duplicates)