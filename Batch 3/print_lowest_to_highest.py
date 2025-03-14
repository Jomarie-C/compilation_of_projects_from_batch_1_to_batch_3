def main():
    numbers = [] 
    
    while True:
        user_input = input("Enter a number: ")
        
        try:
            number = int(user_input)  
            numbers.append(number) 
        except:
            break  
    
    numbers.sort() 
    print("\nNumbers from lowest to highest:", numbers)
    print("\nExiting the program.")

main()
