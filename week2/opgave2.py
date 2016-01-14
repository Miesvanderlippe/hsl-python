__author__ = 'Mies'

from math import pi


def biggerThanFive( toCheck):
    try :
        return float( toCheck) > 5
    except ValueError:
        return False


def smallerThanPi( toCheck):
    try :
        return float( toCheck) < pi
    except ValueError:
        return False


def not42( toCheck):
    try :
        return float( toCheck) != 42
    except ValueError:
        return False


def isOne( toCheck):
    try :
        return float( toCheck) == 1
    except ValueError:
        return False

print( biggerThanFive( 4))
print( biggerThanFive( 5))
print( biggerThanFive( 6.5))

print( smallerThanPi( 3))
print( smallerThanPi( pi))
print( smallerThanPi( 4.5))

print( not42( 41))
print( not42( 42))
print( not42( 43))

print( isOne( -1))
print( isOne( 1))
print( isOne( 2.5))