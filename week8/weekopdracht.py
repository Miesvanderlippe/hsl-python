__author__ = 'Mies'

morse_characters = {
    ' ': '  ',
    ',': '– – . . – – ',
    '.': '. – . – . – ',
    '?': '. . – – . . ',

    '0': '– – – – – ',
    '1': '. – – – – ',
    '2': '. . – – – ',
    '3': '. . . – – ',
    '4': '. . . . – ',
    '5': '. . . . . ',
    '6': '– . . . . ',
    '7': '– – . . . ',
    '8': '– – – . . ',
    '9': '– – – – . ',

    'A': '. – ',
    'B': '– . . . ',
    'C': '– . – . ',
    'D': '– . . ',
    'E': '. ',
    'F': '. . – . ',
    'G': '– – . ',
    'H': '. . . . ',
    'I': '. . ',
    'J': '. – – – ',
    'K': '– . – ',
    'L': '. – . . ',
    'M': '– – ',
    'N': '– . ',
    'O': '– – – ',
    'P': '. – – . ',
    'Q': '– – . – ',
    'R': '. – . ',
    'S': '. . . ',
    'T': '– ',
    'U': '. . – ',
    'V': '. . . – ',
    'W': '. – – ',
    'X': '– . . – ',
    'Y': '– . – ',
    'Z': '– – . .'
}


def main()->None:
    morse = ''
    invalid_chars = False
    word = input('Geef de zin of het woord om te vertalen naar Morse').upper()

    for char in word:
        if char in morse_characters:
            morse += morse_characters[char]
        else:
            invalid_chars = True

    if invalid_chars:
        print('een of meerdere karakters kon niet worden vertaald')

    print(morse)

if __name__ == '__main__':
    main()