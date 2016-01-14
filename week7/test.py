__author__ = 'Mies'

# lijst van 0 - 10 met stappen van 2. Deze syntax is niet belangrijk
test_list = [x for x in range(0, 10, 2)]
test_list_2 = [x for x in range(0, 7, 1)]
superheroes = ['Batman', 'Spongebob', 'Superman', 'Spiderman']

# kan ook mixed types
test_list_3 = [0, 1, 3, 'string', True]

test_string = 'Hallo dit is een test string'

# een element
print(test_list[3])

# een slice (van tot)
print(test_list[3:5])

# vanaf
print(test_list[3:])

# tot
print(test_list[:3])

# maak een list met de getallen 2, 5, 8, 11 (list commando)
print(list(range(2, 12, 3)))

# vanaf achteren
print(test_list[-4])

# aantal items in de list
print(len(test_list))

# Dit werkt ook op een string, dan krijg je de lengte van de string
print(len(test_string))

# optellen van lists (maakt langere list)
print(test_list + test_list_2)

# vermenigvuldigen maakt een langere lijst
print(test_list * 3)


'''
Tussenopdracht :
Maak een functie die alle oneven getallen in de lengte van een woord weergeeft
(Zie einde document)
'''


# geef alle superhelden weer
for held in superheroes:
    print(held)

# kan ook zo (hoeft niet voor toets of whatever)
print(', '.join(superheroes))

# indien niet alleen strings (map voert de functie (param1) uit op de hele list
print(', '.join(map(str, test_list_3)))

# index gebruiken kan ook op een string
print(test_string[2])

'''
Tussenopdracht 2
Vraag 3 woorden aan de gebruiker, zorg dat deze in een list staan
Geeft van ieder woord de laatste letter
Geeft van ieder woord de lengte
(Zie einde document)
'''

# https://docs.python.org/3.4/tutorial/datastructures.html

# append
test_list.append('Zoe')
print(test_list)

# del
del(test_list[2])

# remove (alleen eerste entry)
superheroes.remove('Spongebob')

# pop (geeft het element nog terug in tegenstelling tot del dat niks geeft)
element = test_list.pop(0)

# extend (lijst die eraan moet, zelfde als + maar mooier)
superheroes.extend(['Green Latern', 'The Flash'])

# insert (positie, var)
superheroes.insert(2, 'Patrick')

# sorted (laat lijst zelf onaangepast en geeft nieuwe, gesorteerde lijst)
print(sorted(superheroes))

# .sort() is niet terugdraaibaar maar wel mooier
print(superheroes.sort())

# voor lists met verschillende types weer eerst naar string casten
# er moet eerst een list van gemaakt worden omdat map een object teruggeeft.
print(list(map(str, test_list_3)))

# reverse
print(superheroes.reverse())

# nested lists kunnen ook
nested_list = ['Item 1', 'Item 2', ['Item 3', 'Item 4']]
print(nested_list)

# Haal item 3 uit de nested list
print(nested_list[2][0])

'''
Huiswerk

3e Editie
Hoofdstuk 7

2e
Hoofdstuk 8

AW : 3 t/m 8
PE : 2,4, 7
'''


def even_getallen(word: str)->list:
    """
    :param word: Woord om te tellen
    :return: List met alle even getallen binnen de lengte van het woord
    """
    length = len(word)
    # +1 om ook het laatste even getal in een woord met een even lengte
    number_range = range(2, length+1, 2)
    number_list = list(number_range)

    return number_list


def laatste_letter_lengte_woord(word: str)->tuple:
    """
    :param word: Woord om te tellen en de laatste letter van te geven
    :return: lengte woord, laatste letter woord
    """
    length = len(word)
    last_letter = word[-1]

    return length, last_letter

def main()->None:
    """
    :return:
    """

    print('\033[95mTussenopdrachten:\033[0m')

    # Tussenopdracht 1
    woord = input('Oneven getallen test woord:\n')

    print(even_getallen(woord))

    # Tussenopdracht 2
    woorden = list()
    for i in range(0, 3):
        woord = input('Geef woord {}\n'.format(i+1))

        # append is toevoegen!
        woorden.append(woord)

    # zelfde naam maar gaat goed
    for woord in woorden:

        lengte, laatste_letter = laatste_letter_lengte_woord(woord)

        print('Laatste letter {}:{}'.format(woord, laatste_letter))
        print('Lengte {}:{}'.format(woord, lengte))

if __name__ == '__main__':
    main()