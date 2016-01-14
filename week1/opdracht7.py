__author__ = 'Mies'


miles = input('Please enter the amount of miles driven : \n')
galons = input('Please enter the amount of fuel used in Galons : \n');

try:
    mpg = int( miles)/int( galons)
    print( 'MPG : ' + str( mpg))
except ValueError:
    print( 'Input incorrect. Retry.')
