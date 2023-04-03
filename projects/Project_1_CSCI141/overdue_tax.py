PENALTY_RATE = 0.06 #Do not change
EARTH_YEAR = 365 #Do not change
tax = input('Enter amount of tax owed: ') #Do not change, will be in format $100
rate = input('Enter interest rate: ') #Do not change, will be in format 4%
late = int(input('Enter number of days overdue tax is: ')) #Do not change, will be an integer
tax2=float(tax[1:])
rate2 = float(rate[:-1])
penalty = PENALTY_RATE * float(tax2)
interest = (tax2*(rate2/100))*(late/EARTH_YEAR)
total = round(((tax2) + interest + penalty))
print('Your total payment is ' + str(total))