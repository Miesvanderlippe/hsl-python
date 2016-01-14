__author__ = 'Mies'

from os import path

frame_dict = {
    "TTT": "F|Phe", "TTC": "F|Phe", "TTA": "L|Leu", "TTG": "L|Leu",
    "TCT": "S|Ser", "TCC": "S|Ser", "TCA": "S|Ser", "TCG": "S|Ser",
    "TAT": "Y|Tyr", "TAC": "Y|Tyr", "TAA": "*|Stp", "TAG": "*|Stp",
    "TGT": "C|Cys", "TGC": "C|Cys", "TGA": "*|Stp", "TGG": "W|Trp",
    "CTT": "L|Leu", "CTC": "L|Leu", "CTA": "L|Leu", "CTG": "L|Leu",
    "CCT": "P|Pro", "CCC": "P|Pro", "CCA": "P|Pro", "CCG": "P|Pro",
    "CAT": "H|His", "CAC": "H|His", "CAA": "Q|Gln", "CAG": "Q|Gln",
    "CGT": "R|Arg", "CGC": "R|Arg", "CGA": "R|Arg", "CGG": "R|Arg",
    "ATT": "I|Ile", "ATC": "I|Ile", "ATA": "I|Ile", "ATG": "M|Met",
    "ACT": "T|Thr", "ACC": "T|Thr", "ACA": "T|Thr", "ACG": "T|Thr",
    "AAT": "N|Asn", "AAC": "N|Asn", "AAA": "K|Lys", "AAG": "K|Lys",
    "AGT": "S|Ser", "AGC": "S|Ser", "AGA": "R|Arg", "AGG": "R|Arg",
    "GTT": "V|Val", "GTC": "V|Val", "GTA": "V|Val", "GTG": "V|Val",
    "GCT": "A|Ala", "GCC": "A|Ala", "GCA": "A|Ala", "GCG": "A|Ala",
    "GAT": "D|Asp", "GAC": "D|Asp", "GAA": "E|Glu", "GAG": "E|Glu",
    "GGT": "G|Gly", "GGC": "G|Gly", "GGA": "G|Gly", "GGG": "G|Gly",
}

complimentary = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}


def get_lines_from_file(file_path: str)->list:
    with open(file_path, 'r') as f:
        return f.read().splitlines()


def file_exists(file_path: str)->bool:
    return path.isfile(file_path)


def filter_empty(to_filter: list)->list:
    return [x for x in to_filter if x]


def translatable(string: str)->bool:
    # pep8 really makes my code more readable
    return string.lower().replace('a', '').replace('t', '').replace('c', '')\
        .replace('g', '') == ''


def translate_list(dna: list, shorthand: bool=False)->str:
    string = ''
    for section in dna:
        if len(section) == 3:
            string += frame_dict[section].split('|')[not shorthand]+\
                ['', '  '][shorthand]
    return string


def printable_six_string(string_1: str, string_2: str, short: bool=False)->str:

    side1 = {0: [], 1: [], 2: []}
    side2 = {0: [], 1: [], 2: []}

    printable = []

    for offset in range(0,3):
        for index in range(offset, len(string_1), 3):
            side1[offset].append(string_1[index:index+3])
        for index in range(offset, len(string_2), 3):
            side2[offset].append(string_2[index:index+3])

    for i in range(2, -1, -1):
        printable.append('+'+str(i+1)+(' '*(i+1)) +
                         translate_list(side1[i], short))

    printable.append('   '+string_1)
    printable.append('   '+string_2)

    for i in range(0, 3):
        printable.append('-'+str(i+1)+(' '*(i+1)) +
                         translate_list(side2[i], short))

    return '\r\n'.join(printable)


def complimentary_string(string: str)->str:
    return ''.join(reversed([complimentary[x] for x in string.upper()]))


def main():
    mode = 0

    if mode == 0:
        while True:
            print('menu:')
            print('1) streng invoeren')
            print('2) bestand uitlezen')

            try:
                mode = int(input('\r\nSelecteer een optie:\r\n'))
            except ValueError:
                print('Geen getal gevonden\r\n')
                continue

            if mode not in range(1,3):
                print('Geen geldige selectie\r\n')
                continue

            break

    if mode == 1:

        while True:
            string = input('Voer de DNA streng in:\r\n').upper()
            if translatable(string) and len(string) > 3:
                break
            else:
                print('Deze streng kan niet worden vertaald')

        dna_sec1 = string
        dna_sec2 = complimentary_string(string)

    if mode == 2:
        while True:
            user_path = input('Geef het pad naar het bestand:\r\n')
            if not file_exists(user_path):
                print('Geen bestand gevonden\r\n')
                continue
            else:
                lines = filter_empty(get_lines_from_file(user_path))
                try:
                    if len(lines[0]) > 3:
                        if translatable(lines[0]):
                            print('Succesvol uitgelezen')
                            break
                        else:
                            print('Het gevonden DNA kan niet worden vertaald')
                            continue
                    else:
                        print('Kon niet genoeg tekst vinden in het bestand')
                        continue
                except IndexError:
                    print('Kon geen tekst vinden in het bestand')
                    continue

        dna_sec1 = lines[0]
        dna_sec2 = complimentary_string(lines[0])

    if mode == 1 or mode == 2:
        while True:
            ans = input('Afkortingen gebruikten?\r\n').lower()
            yes = ['ja', 'yes', 'y', '1']
            no = ['nee','no', 'n', '0']
            shorthands = False

            if ans in yes:
                shorthands = True
                break
            elif ans in no:
                shorthands = False
                break
            else:
                print('Geen geldig antwoord gevonden')
                continue

        print(printable_six_string(dna_sec1, dna_sec2, shorthands))

if __name__ == '__main__':
    main()