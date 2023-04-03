D_PER_Y_PLANETS = [87.97, 687, 4331.87, 10760.27, 60189.55] #Do not change
PLANETS = ['Mercury', 'Mars', 'Jupiter', 'Saturn', 'Neptune'] #Do not change
homeNum=int(input('Select your home planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, 4 for Saturn, 5 for Neptune: '))
age=float(input('Enter your age on your home planet: '))
destNum=int(input('Select a destination planet: 1 for Mercury, 2 for Mars, 3 for Jupiter, 4 for Saturn, 5 for Neptune: '))
a=age*D_PER_Y_PLANETS[homeNum-1]
b=int(a/D_PER_Y_PLANETS[destNum-1])
print('Your age on ' + PLANETS[destNum-1] + ' is about',b,'years')
