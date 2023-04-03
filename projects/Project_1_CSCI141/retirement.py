a=int(input('Enter total amount to save: '))
b=int(input('Enter number of paychecks per year: '))
c=(a-((a//b)*(b-1)))

print('You must make ' + str(b-1) +' deductions of $' + str(a//b) + ' and one final deduction of $' + str(c) + ' to save $' + str(a))