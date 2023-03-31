# function to calculate the bill amount and apply discount if applicable
def calculate_bill(clean, cavity, xray):
    total_bill = 0
    
    if clean == 'y':
        total_bill += 60
    if cavity == 'y':
        total_bill += 200
    if xray == 'y':
        total_bill += 100
    
    # add tax to total bill
    total_bill *= 1.15
    
    # Now, apply discount based on bill amount
    if total_bill > 300:
        total_bill *= 0.9
        discount = 10
    elif total_bill > 200:
        total_bill *= 0.95
        discount = 5
    else:
        discount = 0
    
    return (total_bill, discount)

# Let's take input from user
patient_name = input("Enter patient's name: ")
cleaning_performed = input("Was cleaning performed? (y/n): ")
cavity_filling_performed = input("Was cavity-filling performed? (y/n): ")
xray_performed = input("Was X-Ray performed? (y/n): ")

# Now, calculate bill and discount
bill_amount, discount = calculate_bill(cleaning_performed, cavity_filling_performed, xray_performed)

# This is print receipt
print("\nMelanie Dental Clinic")
print("Receipt for patient name:", patient_name)
print("-" * 45)
print("{:<40}{:>5}".format("Subtotal:", "$" + format(bill_amount * 0.85, '.2f')))
print("{:<40}{:>5}".format("Tax:", "$" + format(bill_amount * 0.15, '.2f')))
print("-" * 45)
print("{:<40}{:>5}%".format("Discount (" + str(discount) + "%):", discount))
print("{:<40}{:>5}".format("Total:", "$" + format(bill_amount, '.2f')))
print("-" * 45)

