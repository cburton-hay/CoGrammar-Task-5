import math

# Code used to ask user if they want to invest and get a return on their investment or
# borrow money and calculate their monthly repayments.

print("investment - to calculate the amount of interest you'll earn on your investment\nbond - to calculate the amount you'll have to pay on a home loan")
calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

calculation_type = calculation_type.lower()

if calculation_type == 'investment':

# User will be able to choose how long they want to invest for, interest rate and for how long they want to invest for.

    deposit = int(input("How much money do you wish to deposit?"))


    interest_rate = int(input("What percentage interest rate would you like? Answer as a whole number."))
    interest_rate = interest_rate / 100

    years_of_investment = int(input("How many years to you want to invest for?"))

    interest = input("What style of interest would you like?\nEnter 'simple' or 'compound'")
    interest = interest.lower()

    if interest == 'simple':
        # simple means they will receive the interest on the original deposit.
        amount_simple = deposit * (1 + years_of_investment*interest_rate)
        amount_simple = round(amount_simple, 2)
        print("Returned: " + str(amount_simple))

    elif interest == 'compound':
        # compound means they will build the interest on the new total each year.
        amount_compound = deposit * math.pow(1 + interest_rate, years_of_investment)
        amount_compound = round(amount_compound,2)
        print("Returned: " + str(amount_compound))

    else:
        print("Error")
        
elif calculation_type == 'bond':

    # Borrowing money and making monthly repayments based on the value of the user's house,
    # interest rate and for how many months they want to repay.


    house_value = int(input("How much is your property currently valued for?"))

    interest_rate = int(input("What percentage interest rate would you like? Answer as a whole number."))
    interest_rate = interest_rate / 100/12

    time_years = int(input("How many years to wish to make the repayments?"))

    time_months = time_years * 12

    total_repayments = (interest_rate * house_value)/(1 - (1 + interest_rate)**(-time_months))
    print(f"Your monthly repayments: {total_repayments:,.2f}")
else:
    print("Error")