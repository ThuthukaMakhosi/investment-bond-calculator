#This is a program that allows a user to calculate their interest on an investment or calculate the amount that should be repaid on a home loan each month.
#The user inputs the required values based on whether they chose bond or investment
#Final outputs are rounded off to 2 decimal places to avoid reading a large number of decimals

import math

#Type of calculation to be requested by the user
print('investment - to calculate the amount of interest you will earn on your investment')
print('bond - to calculate the amount you will have to pay on a home loan')

calculation = input('Enter either investment or bond from the menu above to proceed: ').lower()


#this is executed if the user inputs investment 
if calculation == 'investment':
    principal = float(input('Enter deposit amount: '))
    interest_rate = float(input('Enter the interest rate(Do not include %): '))
    years = float(input('Enter invest period in years: '))
    interest = input('Do you want simple or compound interest?: ').lower()


 #this is to allow the user to calculate their investment on simple or compound interest
    if interest == 'compound':
        amount = round(principal * math.pow((1+(interest_rate/100)), years), 2)
        print(f'The total amount is R{amount}')

    elif interest == 'simple':
        amount =round(principal*(1 + (interest_rate/100)*years),2)
        print(f'The total amount is R{amount}')

    else:
        print('Invalid input. Enter simple or compound')

 #this is executed if the user inputs bond 
 #this is to allow the user to calculate the monthly repayments on their bond
elif calculation == 'bond':
    house_value = float(input('Enter the value of the house: '))
    monthly_interest = float(input('Enter the interest rate(Do not include %): '))
    months = float(input('Enter number of months for repayment: '))
    
    repayment = round((((monthly_interest/100)/12)*house_value)/(1 - ((1 + (monthly_interest/100)/12 ))**(-months)), 2)
    monthly_interest
    print(f'The total monthly repayment is R{repayment}')


 #This is executed if the user does not enter the correct input
else:
    print('Invalid input. Please enter investment or bond')