marsYears = int(input('Enter number of Mars years: '))
totalDays = int(marsYears * 687)
earthYears = int(totalDays//365.25)
print('This is about' ,earthYears, 'years on Earth.')