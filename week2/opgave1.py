__author__ = 'Mies'

from random import randint


def throw( t_sides):
    return randint(1, t_sides)


while True:
    try:
        sides = int( input( 'Aantal kanten dobbelsteen \n'))
    except ValueError:
        print( 'Ongeldig aantal kanten')
        continue
    if sides < 2:
        print( 'Ongeldig aantal kanten probeer het opnieuw')
        continue

    print( throw( sides))
