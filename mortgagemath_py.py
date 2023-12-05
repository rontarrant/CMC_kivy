## python mortgage calculation
## The defaults supplied for each entry result in a mortgage payment of $639.81
import math
import string

## Note: the nominal rate is used as a decimal value, NOT a percentage, in order for the math to work
nominalRate = float(input("Interest rate quoted by bank: (Enter for 6.0) ") or "6") / 100
mortgagePrincipal = float(input("Mortgage Principal: (Enter for $125,000) ") or 125000)
downPayment = float(input("Down Payment: (Enter for $25000) ") or 25000)
mortgageAmount = mortgagePrincipal - downPayment
amortizationPeriod = float(input("Amortization Period (in years): (Enter for 25 years) ") or 25)
annualCompoundingPeriods = 2

if(downPayment < (mortgagePrincipal * 0.2)):
	print("HIGH RATIO mortgage")
	cmhcPremium = mortgageAmount * .04
	mortgageAmount += cmhcPremium
else:
	print("LOW RATIO mortgage")

print("nominal rate: ", nominalRate)
print("mortgage amount: ", mortgageAmount)
print("amortization period: ", amortizationPeriod)

amortizationMonths = -(amortizationPeriod * 12)
print("amortizationMonths: ", amortizationMonths)

effectiveRate = math.pow(1 + nominalRate / annualCompoundingPeriods, 2) - 1
print("effective rate: {:0.8f}".format(effectiveRate))

## Calculate the Monthly Periodic Rate (the interest rate that, when compounded monthly, is equal to the effective annual rate)
## There's an anomaly here. To get the same numbers as Alan Marshall, I need to multiply monthlyPeriodicRate by 100, but 
## to get the right outcome, it can't be. That's why the formatted output of monthlyPeriodicRate is done this way in the print() statement.

exponent = 1/12
print("exponent: ", exponent)

monthlyPeriodicRate = math.pow(1 + effectiveRate, exponent) - 1
print("monthly periodic rate: {:0.8f}".format(monthlyPeriodicRate * 10))

monthlyPayment = (monthlyPeriodicRate * mortgageAmount) / (1 - math.pow(1 + monthlyPeriodicRate, amortizationMonths))
print("monthlyPeriodicRate * mortgageAmount: ", (monthlyPeriodicRate * mortgageAmount))
print("(1 - math.pow(1 + monthPeriodicRate, amortizationMonths))", (1 - math.pow(1 + monthlyPeriodicRate, amortizationMonths)))
print("monthly payment: {:0.2f}".format(monthlyPayment))

