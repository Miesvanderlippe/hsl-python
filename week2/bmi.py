__author__ = 'Mies'
__name__ = "__main__"
'''
Calculates BMI using height in M and weight in Kilos
'''


def calcbmi(weight, height):

    try:
        weight = float(weight)
        return float(weight)/(height*height)
    except ValueError:
        return False

'''
Returns string representing weight category using BMI
'''


def bmicat(bmi):
    # determine weight category (if only we could use a switch :((
    try:
        if bmi < 18.5:
            return "U heeft ondergewicht"
        elif bmi < 25:
            return"U heeft een gezond gewicht"
        elif bmi < 30:
            return "U heeft overgewicht"
        else:
            return "U heeft zwaar overwicht (obesitas)"
    except ValueError:
        return False

'''
Asks for user input which must be a valid float.
msg          = text before input
positive     = whether input must be > 0
errormsg     = message shown when input isn't a valid float
notposmes    = message shown when input is not more than zero
'''


def numeral_input( msg="Please enter a valid number.\n", positive = False, errormsg="Can't convert to number, please try again. \n", notposmes = "Number is not more than zero, please try again."):
    while True:

        inputval =  input( msg)

        try:
            floatinput = float(inputval)

            if positive and floatinput < 0:
                print(notposmes)
                continue

            return floatinput
        except ValueError:
            print(errormsg)
            continue

'''
Main program loop.

Asks for input in form of length(CM) and weight(KG), gives BMI and BMI cat.
'''


def main():
    while True:

        # Get length and weight.
        length = numeral_input("Lengte in centimeters\n", True, "Kon het getal niet converteren. Probeer het opnieuw.", "Getal moet meer dan 0 zijn. Probeer het opnieuw.")
        weight = numeral_input("Gewicht in kilogram\n", True, "Kon het getal niet converteren. Probeer het opnieuw.", "Getal moet meer dan 0 zijn. Probeer het opnieuw.")

        # Nothing can go wrong here but still.
        try:
            # convert length from cm to m
            length = int(length)/100
            weight = float(weight)

            bmi = calcbmi(weight, length)

            # should never happen either.
            if type(bmi) == "bool":
                print("Kon BMI niet berekenen. Probeer het opnieuw.\n")
                continue

        except ValueError:
            # Try again mes
            print("Kon BMI niet berekenen. Probeer het opnieuw.\n")
            continue

        # output raw BMI
        print("BMI : "+str(bmi))

        # output BMI in string
        print(bmicat(bmi))

        print("\n~~========~~\n\nU mag nog een keer!\n\n~~========~~\n")

if __name__ == "__main__":
    main()
