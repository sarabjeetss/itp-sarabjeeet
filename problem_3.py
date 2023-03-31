'''Create a Python script for the COUNT A DOLLAR game.'''
# Values from the question
PENNY_VALUE  = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# Now take values from the user 
def takeInput():
    pennies = int(input("Enter number of pennies: \n"))
    nickels = int(input("Enter number of nickels: \n"))
    dimes = int(input("Enter number of dimes: \n"))
    quarters = int(input("Enter number of quarters:\n "))
    return pennies, nickels, dimes, quarters


# Function to perform calculations and display result
def countADollar():
    pennies, nickels, dimes, quarters = takeInput()
    totalCent = pennies * PENNY_VALUE + nickels * NICKEL_VALUE + dimes * DIME_VALUE + quarters * QUARTER_VALUE
    totalDollars = totalCent / PENNIES_IN_DOLLAR
    if totalDollars > 1.0:
        print("Sorry, the amount you entered was more than one dollar.\n:( ")
    elif totalDollars < 1.0:
        print("Sorry, the amount you entered was less than one dollar.\n:(")
    else:
        print("Congratulations!\nThe amount you entered was exactly one dollar!\nYou win the game!!/n:)")

# Main program
countADollar()