print("Enter ten(10) numbers:")

odd_count = 0

for i in range(1, 11):
    num = int(input(f"Enter a number ({i} of 10): "))
    if num % 2 != 0:
        odd_count += 1

print("The value of odd numbers in the given set is", + odd_count)