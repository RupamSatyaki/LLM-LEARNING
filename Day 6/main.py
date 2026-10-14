from math_utils import add, subtract
from InquirerPy import inquirer


def get_numbers():
    nums = []

    while True:
        num = input("Enter your number (or 'end' to stop): ").strip().lower()

        if num == "end" or num == "exit":
            print("all numbers: ", nums)
            break

        if num.isdigit(): 
            nums.append(int(num))
            print(nums)

    

    return nums
    
def get_number():
    while True:
        num_1 = input("Enter your first number: ")
        if num_1.isdigit():
            num1 = int(num_1)
            break
        else:
            print("Invalid Input! Please enter a valid number. ")

    while True:
        num_2 = input("Enter your secound number: ")
        if num_2.isdigit():
            num2 = int(num_2)
            break
        else:
            print("Invalid Input! Please enter a valid number. ")

    return num1, num2


choice = inquirer.select(
    message="Modular Math Function Library",
    choices=[
        "Add(a + b)",
        "Subtract(a - b)",
        "Multiply(a * b)",
        "Divide(a / b)",
        "is_even(number)",
        "is_prime(number)",
        "factorial(number)",
        "average(numbers)",
    ]
).execute()


print(choice)


if choice == "Add(a + b)":
    nums = get_numbers()
    result = add(nums)
    print("Sum of all numbers is: ", result)
elif choice == "Subtract(a - b)":
    num1, num2 = get_number()
    result = subtract(num1, num2)
    print("Subtract of all numbers is: ", result)

