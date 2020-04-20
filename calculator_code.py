"""
This is a simple calculator function in python for learning purpose. 
"""
# Just print a line with print function
print("************ Welcome to Rashid Bilgrami Calculation ***********\n")

# Collecting first value as input from the the user
try:
    firstNumber = int(input("Please Type Your First Number: "))
except:
    print(
        "First Number Must be Only Numbers, May be You entered the Characters Like Abc or any special character"
    )
    firstNumber = int(input("Please Type Your First Number: "))

# Collecting second value as input from the the user
try:
    secondNumber = int(input("Please Type Your Second Number:  "))
except:
    print(
        "For Calculator, I required number, but i found you have supplied some character. Please enter only numbers like 1 2 3"
    )
    secondNumber = int(input("Please Type Your Second Number:  "))


# Collecting what calculation method a user required suppling as an input
try:
    calMethod = int(
        input(
            "Please Select The Function You Need To Perform? Please use the below requested number\n 1 is for Addition \n 2 for Subtract \n 3 for Multiplication \n 4 for Division \n 5 For Reminder \n Your Choice: "
        )
    )
except:
    print(
        "Sorry you did not enter the correct option. Please use the below requested number\n 1 is for Addition \n 2 for Subtract \n 3 for Multiplication \n 4 for Division  \5 For Reminder  \n Your Choice:"
    )
    calMethod = int(input("Please Select The Function You Need To Perform?  "))

# Calculation Start
if calMethod == 1:
    print("Your Answer is \n" + str(firstNumber + secondNumber))
elif calMethod == 2:
    print("Your Answer is \n" + str(firstNumber - secondNumber))
elif calMethod == 3:
    print("Your Answer is \n" + str(firstNumber * secondNumber))
elif calMethod == 4:
    try:
        print("Your Answer is \n" + str(firstNumber / secondNumber))
    except:
        print("Your Answer is '0', You can't divide by zero with any number with zero")

elif calMethod == 5:
    try:
        print("Your Answer is \n" + str(firstNumber % secondNumber))
    except:
        print("Your Answer is '0', You can't divide by zero with any number with zero")


# Program End
# Note: As goto method is not in the python we can use while until the user supply the correct input format value
