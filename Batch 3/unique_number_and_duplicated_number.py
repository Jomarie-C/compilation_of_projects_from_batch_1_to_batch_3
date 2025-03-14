numbers = []

for i in range(1, 11):
    try:
        num = int(input(f"Enter a number({i} of 10): "))    
        if numbers.count(num) == 0:
            print("Unique")
        else:
            print("Duplicate")
        numbers.append(num)
    
    except ValueError:
        print("Invalid input, stopping.")
        break  