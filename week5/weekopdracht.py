__author__ = 'Mies'

'''
Inleveropdracht Week 5, Pyramide/diamant:
Schrijf een programma dat aan de gebruiker een getal vraagt. Hij toont dan een pyramide patroon op basis van dit getal, waarbij het ingevoerde getal boven staat en elke opvolgende regel dit getal met 1 eenheid minder. Als de gebruiker geen getal invoert, dan verschijnt de melding: “Helaas geen getal!. Probeer opnieuw!”. De gebruiker moet dan opnieuw een getal invoeren.
Als voorbeeld:
Voer een getal in: 4
   4
  333
 22222
1111111

Nog een voorbeeld:
Voer een getal in: A “Helaas geen getal!. Voer een getal in: 2
 2
111

Nog een voorbeeld:
Voer een getal in: 5
    5
   444
  33333
 2222222
111111111

Probeer opnieuw!”
Nog een voorbeeld:
Uitdaging aan de studenten (voor 60 binpunten):
Er moet in plaats van een pyramide een diamant getoond worden: Voer een getal in: 5

    5
   444
  33333
 2222222
111111111
 2222222
  33333
   444
    5
'''


# asks for a numeral input, performs several checks if asked to.
def numeral_input( msg="Please enter a valid number.\n",
                   positive=False,
                   roundnumber = False,
                   errormsg="Can't convert to number, please try again. \n",
                   notposmes="Number is not more than zero, please try again."):
    while True:

        inputval =  input( msg)

        try:
            if(roundnumber):
                floatinput = int(inputval)
            else:
                floatinput = float(inputval)

            if positive and floatinput < 0:
                print(notposmes)
                continue

            return floatinput
        except ValueError:
            print(errormsg)
            continue


# draws pyramid
def drawpyramid(max):
    for i in range(1, max+1):
        spacesinfront   = (max-i)
        characters      = ((i*2)-1)
        print(' ' * spacesinfront + str(i)*characters)


# draws pyramid, followed by inverted pyramid minus bottom layer.
def drawdiamond(max):
    drawpyramid(max)
    for i in range(max-1, 0, -1):
        spacesinfront   = (max-i)
        characters      = (i*2)-1
        print(' ' * spacesinfront + str(i)*characters)


# asks for user input, draws a diamond
def main() -> None:
    pyramidemax = numeral_input('Geef het formaat van de pyramide\n', True, True, 'Kan niet converteren naar geldig, heel getal. Probeer het opnieuw.\n', 'Getal is niet meer dan 0, probeer het opnieuw.')
    drawdiamond(pyramidemax)

if __name__ == '__main__':
    main()
