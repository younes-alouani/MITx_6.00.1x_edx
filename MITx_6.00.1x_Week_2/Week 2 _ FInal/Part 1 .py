# -*- coding: utf-8 -*-
"""
This code calculate the credit card balance after one year if a person only
pays the minimum monthly payment required by the credit card company each 
month.
The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

    monthlyPaymentRate - minimum monthly payment rate as a decimal

"""

# Values at month 0

month_number = 0 

while month_number < 12 :
    month_number += 1
    balance = balance * (1 - monthlyPaymentRate) #new balance after payment
    balance = balance *- (1 + annualInterestRate/12) #new balance including interest
    
balance = round(balance,2)
print("Remaining balance: ",balance)


