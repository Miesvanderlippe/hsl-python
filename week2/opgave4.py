__author__ = 'Mies'

from random import randint

while True:

    randint1 = randint(0, 20)
    randint2 = randint(0, 20)

    print('Wat is ' + str( randint1) + ' + ' + str(randint2))

    try:
        answer = float( input( 'Antwoord: \n'))
    except ValueError:
        print( 'Ongeldig geteal, nieuwe opdracht')
        continue

    if( (randint1 + randint2) == answer):
        print('Correct!')
    else:
        print('Incorrect, nieuwe opdracht')