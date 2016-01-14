__author__ = 'Mies'

import re
import os.path

knipeiwitten = [
    {
        'short':    'EcoRI',
        'name':     'Escherichia coli',
        'seq':      'GAATTC',
        'offset':   1
    },
    {
        'short':    'EcoRII',
        'name':     'Escherichia coli',
        'seq':      'CCWGG',
        'offset':   0
    },
    {
        'short':    'BamHI',
        'name':     'Bacillus amyloliquefaciens',
        'seq':      'GGATCC',
        'offset':   1
    },
    {
        'short':    'HindIII',
        'name':     'Haemophilus influenzae',
        'seq':      'AAGCTT',
        'offset':   1
    },
    {
        'short':    'NotI',
        'name':     'Nocardia otitidis',
        'seq':      'GCGGCCGC',
        'offset':   2
    }
]


# http://stackoverflow.com/questions/3873361/finding-multiple-occurrences-of-a-string-within-a-string-in-python
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


def filepath_input(msg="Please enter the file path.\n",errormsg="Can't find the file specified. Please try again. \n"):
    while True:
        path = input(msg)

        if file_exists(path):
            return path
        else:
            print(errormsg)


def file_exists(path):
    return os.path.isfile(path)


def get_lines_from_file(path):

    if file_exists(path):
        with open(path) as f:
            lines = f.readlines()

        return lines
    else:
        return False


def get_sequence_index():
    i = 0
    for eiwitarray in knipeiwitten:
        i += 1
        print(str( i), eiwitarray['name'], '('+eiwitarray['short']+')', 'sequence:'+eiwitarray['seq'])

    print('\n')

    while True:
        selected = numeral_input('Selecteer een enzym\n')

        if i < selected or selected < 1:
            print('Enzym niet gevonden in lijst met enzymen.\n')
            continue
        else:
            return int(selected)
            break



def main():
    print('\n====\n\033[95mWelkom bij de knipshow. \033[0m\n====\n')

    selected = get_sequence_index()
    selected = knipeiwitten[selected-1]

    sequences = get_lines_from_file(filepath_input())

    i = 0
    for sequence in sequences:
        i += 1
        print('Regel:', i)
        sequence = sequence.upper()

        found = False

        for m in re.finditer(selected['seq'], sequence):
            found = True
            print(selected['name']+' knipt op positie :', m.start()+selected['offset'])

        for m in re.finditer(selected['seq'][::-1], sequence):
            found = True
            print(selected['name']+' knipt op positie :', m.start() + (selected['seq'].len() - selected['offset']))

        if not found:
            print('Niks gevonden')

if __name__ == '__main__':
    while True:
        main()
        input('press enter to continue')