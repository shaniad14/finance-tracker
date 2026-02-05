"""
FINANCE TRACKER
this asks the user for a budget and then tells them how they are doing.
"""

# Ask user for monthly allowance
allowance = round(float(input("Enter your monthly allowance($): ")),2)

# Ask for expenses
clothes = float(input("How much did you spend on clothing($)? "))
food = float(input("How much did you spend on food($)? "))
gas = float(input("How much did you spend on gas($)?"))


# Calculate total expenses
total_expenses = clothes + food + gas


# Calculate remaining balance
balance = allowance - total_expenses

# Dispaly results
print("\n---Monthly Summary---")
print("Allowance: $" + str(allowance))
print("Total expenses: $" + str(total_expenses))
print("Remaining balance: $" + str(balance))


# Display message based on balance
if balance > 0:
    print("Nice work! You are below budget!")
elif balance == 0:
    print("Good, but be careful because you spent all your money.")
else:
    print("uh oh! You spent more than you have. You'll need to work to pay of your debt!")
    