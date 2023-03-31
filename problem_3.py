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