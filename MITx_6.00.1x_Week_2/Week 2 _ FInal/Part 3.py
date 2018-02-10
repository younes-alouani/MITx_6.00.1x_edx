# -*- coding: utf-8 -*-
"""
This code calculates the minimum fixed monthly payment needed in order 
pay off a credit card balance within 12 months. By a fixed monthly payment, 
we mean a single number which does not change each month, but instead is 
a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

    balance - the outstanding balance on the credit card

    annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will 
pay off all debt in under 1 year

"""

# Values at month 0

Lowest_Payment = 0 
month_number = 0
vbalance = balance
monthlyInterestRate = annualInterestRate/12

#lower and upper bound payment
lowerBoundPayment = balance / 12
upperBoundPayment = (balance * (1 + monthlyInterestRate)**12)/12

while vbalance != 0 :
    vbalance = balance
    month_number = 0
    Lowest_Payment = (lowerBoundPayment + upperBoundPayment)/2
    while month_number < 12 :
        month_number += 1
        vbalance = vbalance - Lowest_Payment #new balance after payment
        vbalance = vbalance * (1 + annualInterestRate/12) #new balance including interest
    vbalance = round(vbalance,2) 
    if vbalance > 0 :
        lowerBoundPayment = Lowest_Payment
    if vbalance < 0 :
        upperBoundPayment = Lowest_Payment

Lowest_Payment = round(Lowest_Payment,2)
print("Lowest Payment: ",Lowest_Payment)
