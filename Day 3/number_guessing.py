import random

def main():
    
    # define a random number
    secretNumber = random.randint(1, 100)

    attempt = 1

    
    while attempt <= 7:
        print("Attempt Count: ", attempt)
        while True:
            guessInput = input("Guess a number between 1 and 100: ")

            if guessInput.isdigit():
                guess = int(guessInput)
                break
            else:
                print("Invalid input! Please enter only numbers.")
    
        
        if guess == secretNumber:
            print("Congratulations")
            break
        elif guess <= secretNumber:
            print("Too Low")
        elif guess >= secretNumber:
            print("Too High")

        attempt = attempt + 1

    if attempt > 7:
        print("game over")


    while True: 
        restartInput = input("Would you like to restart the game, please respond with yes or no: ")

        retsart = restartInput.lower()

        if retsart == "yes":
            main()
            break
        elif retsart == "no":
            break
        else:
            print("Invalid Input! Please enter valid input")
    

main()