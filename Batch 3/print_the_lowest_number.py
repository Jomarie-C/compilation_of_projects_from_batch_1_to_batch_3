lowest_number = float('inf')

while True:
    user_input = input("Enter a number: ")
        
    if user_input.isdigit():
        number = int(user_input)
    elif number < lowest_number:
        lowest_number = number
    else:
        break