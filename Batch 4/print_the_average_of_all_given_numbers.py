numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

if len(numbers) > 0:
    total = sum(numbers)
    average = total / len(numbers)
    print("Average of the numbers:", average)
else:
    print("No numbers entered.")