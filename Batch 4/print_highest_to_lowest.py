numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

numbers.sort()
numbers.reverse()

print("\nNumbers from highest to lowest:", numbers)
print("\nExiting the program")