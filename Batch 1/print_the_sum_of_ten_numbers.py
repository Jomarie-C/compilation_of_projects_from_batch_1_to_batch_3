print("SUMMATION OF TEN(10) NUMBERS")
print("\nEnter ten(10) numbers: ")

sum_of_ten_numbers = 0
for i in range(1, 11):
    num = float(input(f"Enter a number ({i} of 10): "))
    sum_of_ten_numbers += num

print("The sum of ten numbers is", + sum_of_ten_numbers)