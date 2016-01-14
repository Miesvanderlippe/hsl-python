__author__ = 'Mies'


def numeral_input( msg="Please enter a valid number.\n",
                   positive = False,
                   errormsg="Can't convert to number, please try again. \n",
                   notposmes = "Number is not more than zero, please try again."):
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

# main program
def main():

    # introduce ourselves
    print('\n====\n\033[95mDit programma demonstreert een aantal simpele vergelijkingen. Hiervoor hebben we vier getall'
          'en nodig, vul deze in waneer daarnaar gevraagd word.\033[0m\n====\n')
    while True:

        # Ask user for 4 numbers
        var1 = numeral_input("Voor het eerste getal in\n")
        var2 = numeral_input("\nVoor het tweede getal in\n")
        var3 = numeral_input("\nVoor het derde getal in\n")
        var4 = numeral_input("\nVoor het vierde getal in\n")

        # als var1<=var2 en var2 != var1 wordt het getal ‘1’ getoond. 
        if var1 < var2:
            print("1")

        # Some space before asking questions
        print("\n")

        #  Als var3>var1 of var2 == var4 wordt het getal ‘2’ getoond 
        if var3 > var1 or var2 == var4:
            print("2")

        # Als (var4 < var3 of var2>var1) en (var4 < var1) dan wordt er ‘3a’ getoond.
        if (var4 < var3 or var2 > var1) and (var4 < var1):
            print("3a")

        # Anders als (var4 < var3 en var2>var1) of (var4 < var1) wordt er ‘3b’ getoond.
        elif (var4 < var3 and var2 > var1) or ( var4 < var1):
            print("3b")

        # Kloppen beiden niet dan krijg wordt er ‘3c’ getoond 
        else:
            print("3c")

        print("\nU kan het programma nog een keer doorlopen met nieuwe getallen. \n")


if __name__ == "__main__":
    main()