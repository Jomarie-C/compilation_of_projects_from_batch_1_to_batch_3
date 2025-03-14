numbers = []

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

most_common = None
max_count = 0

for num in numbers:
    count = numbers.count(num)
    if count > max_count:
        max_count = count
        most_common = num

if max_count > 1:
    print("The most common number entered is", most_common)
else:
    print("No duplicates found.")