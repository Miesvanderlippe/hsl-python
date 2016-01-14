__author__ = 'Mies'

'''
Population
Write a program that predicts the appropiate size of a population of organism. The shown number should be rounded up in 2 decimals. The application should use text boxes to allow the user to enter the starting number of organisms, the average daily increase (as a percentage), and the number of days the organisms will be left to multiply. For example, assume the user enters the following values:
Starting number of organisms: 2 Average daily increase: 30 Number of days to multiply: 10
The program should display the following table of data:
Day Approximate Population 1 2.00
2 2.60
3 3.38
4 4.39 5 5.71 6 7.43 7 9.65 8 12.55 9 16.31 10 21.21
Exercise courtesy from ‘Starting out with python’, third edition
'''


def numeral_input( msg="Please enter a valid number.\n",
                   positive=False,
                   errormsg="Can't convert to number, please try again. \n",
                   notposmes="Number is not more than zero, please try again."):
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


def increase_population(cur_pop: float, incr_factor: float) ->float:
    return cur_pop*incr_factor


def percentage_to_factor(percentage: float) ->float:
    return float(percentage/100)+1


def main() -> None:
    starting_population =           numeral_input('Current population\n', True)
    increase_factor =               percentage_to_factor(numeral_input('Daily increase in percent\n', True))
    days_left =                     int(numeral_input('Days left\n', True))
    population_after_increase =     starting_population

    for i in range(1, days_left + 1):
        population_after_increase = increase_population( population_after_increase, increase_factor)
        print('Na {} dag(en) is de bevolking : {:.2f} eenheden groot'.format(i, population_after_increase))

if __name__ == "__main__":
    main()