__author__ = 'Mies'

#recipe
cupsOfSugar  = float(1.5)
cupsOfButter = float(1)
cupsOfFlour  = float(2.75)

amountOfCookiesPerRecipe = float(48)

amountOfCookiesDesired = input('How many cookies do you want to make?\n')

try:
    #tryin to convert input amounts
    amount = float(amountOfCookiesDesired)
    print( 'Sugar : ' + str( (cupsOfSugar / amountOfCookiesPerRecipe) * amount) + 'cups')
    print( 'Butter : ' + str( (cupsOfButter / amountOfCookiesPerRecipe) * amount) + 'cups')
    print( 'Flour : ' + str( (cupsOfFlour / amountOfCookiesPerRecipe) * amount) + 'cups')
except ValueError:
    #could use a way to return to the front of the script
    print('couldn\'90t calculate amounts')
