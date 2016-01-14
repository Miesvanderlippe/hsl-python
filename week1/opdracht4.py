__author__ = 'Mies'


'''
totalItems = 0;
totalPrice = float( 0)

while totalItems < 5:

    inputVal =  input('Price of item ' + str( totalItems + 1) + '\n')

    try:
        floatInput = float( inputVal)
    except ValueError:
        print('Can\'t convert to number, try again')
        continue

    if floatInput > 0:
        totalPrice += floatInput
        totalItems += 1
    else:
        print('Price is below zero. Please enter a positive number')
        continue

print( 'Subtotal : \n' + str( totalPrice))
print( 'Tax (7%) : \n' + str( totalPrice * 0.07))
print( 'Total : \n' + str( totalPrice * 1.07))
'''


def numeral_input( msg, errormsg="Can't convert to number, please try again. \n"):
    while True:

        inputval =  input( msg)

        try:
            floatinput = float(inputval)
            return floatinput
        except ValueError:
            print(errormsg)
            continue

print(numeral_input('test\n'))