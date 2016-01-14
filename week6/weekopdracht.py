from random import randint

__author__ = 'Mies, Jeroen, Owain, Dennis, Luka'


def hl(h_naam_speler):
    """
    :param h_naam_speler: Naam speler van het spel.
    :return: Behaalde score

    Deze functie print een random getal tussen 1 en 20 en neemt een input.
    De gebruiker antwoordt "h" of "l", op basis van de gedachten van de gebruiker of het volgende getal hoger of
    lager is. Als het fout is stopt de functie en als er vijf punten behaald zijn ook.
    """
    h_getal_2 = randint(1, 20)
    for h_punten in range(0, 5):
        h_getal_1, h_getal_2 = h_getal_2, randint(1, 20)
        print("Het getal is:", h_getal_1)
        h_inp = input("%s, wat denk jij, is het getal hierna hoger of lager? (h/l)\n" % h_naam_speler)
        if h_getal_1 == h_getal_2:
            print("\nHet getal is even hoog. Je krijgt een punt!\n")
        elif (h_inp == "h" and h_getal_2 > h_getal_1) or (h_inp == "l" and h_getal_2 < h_getal_1):
            print("{}, dat klopt!".format(['Hoger', 'Lager'][h_inp == 'l']))
        else:
            print("\nHelaas, niet goed. Je hebt het {} ronden volgehouden. Het was getal {}\n".format(h_punten,
                                                                                                  h_getal_2))
            return h_punten
    print("\nHet spel is afgelopen. Je hebt", h_punten + 1, "punten behaald!\n")
    return h_punten + 1


def gooi_afhandelen(g_speler1, g_speler2, g_random, g_score1):
    """
    :param g_speler1: Naam speler 1
    :param g_speler2: Naam speler 1
    :param g_random:  Worp speler 2
    :param g_score1:  Worp speler 1
    :return: Winnaar, score

    Vergelijkt worpen en geeft aan de hand daarvan een winnaar en een score. Wanneer gelijk word gegooid
    word er true teruggegeven waarna opnieuw kan worden gegooid.
    """
    print(g_speler1 + " gooit een " + str(g_score1))
    print(g_speler2 + " gooit een " + str(g_random))

    if g_score1 == g_random:
        print("Gelijke score! We gooien nog een keer.")
        return True
    else:
        if g_score1 > g_random:
            print(g_speler1 + " heeft gewonnen!")
            return g_speler1, g_score1
        else:
            print(g_speler2 + " heeft gewonnen!")
            return g_speler2, g_random


def hoogste_gooit(h_speler1, h_speler2):
    """
    :param h_speler1: Naam speler1
    :param h_speler2: Naam speler2
    :return: Winaar, score

    Speelt het Hoogste gooit spel met 2 spelers tot er niet gelijk word gespeeld.
    """
    h_draw, h_score1 = True, 0

    while h_draw:
        for h_i in range(1, 3):
            h_random = randint(1, 6)

            if h_i == 1:
                h_score1 = h_random
            else:
                h_value = gooi_afhandelen(h_speler1, h_speler2, h_random, h_score1)

                if h_value != True:
                    return h_value


def raden(r_speler1, r_speler2):
    """
    :param r_speler1: Naam speler 1
    :param r_speler2: Naam speler 2
    :return: Winaar, score

    Laat 2 spelers een getal raden. Wanneer een speler het goed raad is het spel afgelopen.
    Waneer geen van beide spelers het goed raad word er nog een ronde vragen gesteld tot het getal
    wel goed word geraden.
    """
    r_winnaar = 0
    print('Wie raadt als eerste het getal onder de 10?')
    while r_winnaar == 0:
        r_antwoord1 = numeral_input(r_speler1 + ' wat denk jij dat het is?\n', True, True, 'Geen geldig getal',
                                    'Geen positief getal')
        r_antwoord2 = numeral_input(r_speler2 + ' wat denk jij dat het is?\n', True, True, 'Geen geldig getal',
                                    'Geen positief getal')
        r_randomNummer = randint(1, 10)
        if r_randomNummer == r_antwoord1:
            print('De winnaar is', r_speler1, 'met getal', str(r_randomNummer))
            r_winnaar = 1
        elif r_randomNummer == r_antwoord2:
            print('De winnaar is', r_speler2, 'met getal', str(r_randomNummer))
            r_winnaar = 2
    return r_winnaar, 5


def get_name(g_msg='Enter name:\n'):
    """
    :param g_msg: (optioneel) boodschap die moet worden weergegeven
    :return: een string langer dan 0 tekens.
    """
    g_name = ''
    while len(g_name) < 1:
        g_name = input(g_msg)
    return g_name


def numeral_input(n_msg="Please enter a valid number.\n",
                  n_positive=False,
                  n_roundnumber=False,
                  n_errormsg="Can't convert to number, please try again. \n",
                  n_notposmes="Number is not more than zero, please try again."):
    """
    :param n_msg: Vraag die gesteld word
    :param n_positive: Of het getal positief moet zijn
    :param n_roundnumber: Of het een heel getal moet zijn
    :param n_errormsg: Het bericht dat word weergegeven als het getal niet klopt
    :param n_notposmes: Het bericht wat word weergegeven als het getal niet boven 0 is
    :return: int of float (de input)

    Vraagt de gebruiker om een geldig getal tot aan alle voorwaarden word voldaan.

    TODO:
    - Range param
    """
    while True:

        n_inputval = input(n_msg)

        try:
            if n_roundnumber:
                n_floatinput = int(n_inputval)
            else:
                n_floatinput = float(n_inputval)

            if n_positive and n_floatinput < 0:
                print(n_notposmes)
                continue

            return n_floatinput
        except ValueError:
            print(n_errormsg)
            continue

"""
Unused
def get_length_longest_entry(g_array, g_field):
    g_longest = 0
    for g_entry in g_array:
        if len(g_entry[g_field]) > g_longest:
            g_longest = len(g_entry[g_field])
    return g_longest


def scoreboard(s_scores, s_players):
    s_longestname = get_length_longest_entry(s_scores, 'playername')
    s_longestgame = get_length_longest_entry(s_scores, 'game')

    print(s_longestname)
"""


def main():
    """
    :return: void

    Speelt alledrie de spelletjes en geeft nadat er door een van de spelers 10 punten
     of meer is gehaald de eindscore weer.
    """
    # Get playername
    player1, player2 = get_name('Naam speler 1\n'), get_name('Naam speler 2\n')

    # Scores
    score_player1, score_player2 = 0, 0

    while score_player1 < 10 and score_player2 < 10:

        # Bericht
        if score_player1 > 0 and score_player2 > 0:
            print('\nEr zijn niet genoeg punten gehaald in de vorrige ronde. Er word nog een ronde '+
                  'spelletjes gespeeld!\n')

        # Game 1
        print('\nSpel 1 : Raad het getal\n')
        winnaar, score = raden(player1, player2)
        if winnaar == 1:
            score_player1 += score
        else:
            score_player2 += score

        # Game 2
        print('\nSpel 2 : Wie gooit het hoogste?\n')
        winnaar, score = hoogste_gooit(player1, player2)

        if winnaar == player1:
            score_player1 += score
        else:
            score_player2 += score

        # Game 3
        print('\nSpel 3 : Hoger of lager?\n')
        score_player1, score_player2 = hl(player1) + score_player1, hl(player2) + score_player2

    # Scores

print('Scores : \n{} : {} \n{} : {}'.format(player1, score_player1, player2, score_player2))


if __name__ == '__main__':
    main()