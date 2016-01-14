from timeit import timeit

'''
Opdracht 2
Deze opdracht is een raadsel. Als je de opdracht goed uitvoert, vind je een codewoord. Degene die het juiste codewoord als eerste naar de docent weet te mailen, verdient 100 binpunten.

Op ELO staan twee bestanden (bestand1.txt en bestand2.txt). Deze bestanden staan vol met woorden. Zoek uit of er woorden zijn die in allebei de bestanden voorkomen. Als je deze woorden hebt gevonden, neem dan de langste twee woorden hiervan en kijk of er letters zijn die in het ene woord wél voorkomen en in het andere niet. Deze letters vormen een anagram. Nu heb je genoeg informatie om het codewoord te achterhalen.
'''


def get_lines_from_file(file_path: str)->None:
    with open(file_path, 'r') as f:
        return f.read().splitlines() # super fancy file functies


def ben1(l1: list, l2: list)->bool:

    col = []
    for item in l1:
        if item in l2:
            col.append(item)

    return True


def ben2(s1: set, s2: set)->bool:

    col = s1.intersection(s2)
    return True


def main()->None:

    # bestanden lezen, we maken sets van de woorden
    l1 = get_lines_from_file('1.txt')
    l2 = get_lines_from_file('2.txt')

    s1 = set(l1)
    s2 = set(l2)

    # print(timeit(lambda: ben1(l1, l2), number=1000))
    # print(timeit(lambda: ben2(s1, s2), number=1000))


    # dit zijn de woorden die in beide voorkomen
    in_both = list(s1.intersection(s2))
    print(in_both)

    # ik sorteer de lijst met de computer maar kan natuurlijk handmatig
    in_both.sort(key=len)
    in_both.reverse() # langste eerst

    # we maken sets van de langste twee woorden
    longest_1 = set(in_both[0])
    longest_2 = set(in_both[1])

    # van die sets nemen we het verschil
    secret_word = longest_1.difference(longest_2)

    # we printen de hele zooi zonder spaties
    print(''.join(secret_word))

if __name__ == '__main__':
    main()
