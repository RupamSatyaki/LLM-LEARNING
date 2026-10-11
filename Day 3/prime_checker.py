def main():
    while True:
        numberInput = input("enter a number: ")

        if numberInput.isdigit():
            number = int(numberInput)
        else:
            print("That is not a positive number. Try again.")

        if number > 0:
            break
        else:
            print("Invalid input! Please enter a valid integer.")


    if number < 2:
        print("Not Prime")
    elif number == 2:
        print("Prime")
    else:

        is_prime = True
        for i in range(2, int(number * 0.5)):
            if number % i == 0:
                is_prime = False
                # break
    
        if is_prime:
            print("Prime")
        else:
            print("Not Prime")


    while True: 
        restartInput = input("Would you like to check one more number, please respond with yes or no: ")

        retsart = restartInput.lower()

        if retsart == "yes":
            main()
            break
        elif retsart == "no":
            break
        else:
            print("Invalid Input! Please enter valid input")
    


main()