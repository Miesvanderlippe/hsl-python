from random import getrandbits, shuffle


# geeft True of False terug
def rand_bool()->bool:

    # een bit is 0 of 1, ik vraag 1 willekeurige bit op
    return getrandbits(1) == 1


def main()->None:

    # spelers
    players = ['Mies', 'Monika']

    # scores = {Mies:0, Monika:0}, kan ook handmatig, van te voren
    scores = {x: 0 for x in players}

    # sorteerd een lijst op willekeurige volgorde
    shuffle(players)

    # word op True gezet wanneer het spel voorbij is
    game_over = False

    # zolang het spel niet voorbij is
    while not game_over:

        # gooit elke speler
        for player in players:

            # tenzij het spel voorbij is
            if game_over:
                break

            # elke speler gooit 3 keer
            for throw in range(1, 4):

                # met 50/50 kans raak te gooien
                if rand_bool():

                    # als er raak wordt gegooit:
                    print('{} hits {}'.format(player, scores[player]+1))
                    scores[player] += 1

                    # als de score 20 is geworden is het spel voorbij
                    if scores[player] == 20:
                        print('{} wins the game'.format(player))

                        # en word game_over op true gezet wat alle loops stopt
                        game_over = True
                        break
                else:

                    # wanner er mis wordt gegooit
                    print('{} misses {}'.format(player, scores[player]+1))

            # lijntje tussen de speler
            print('\r\n--------\r\n')


if __name__ == '__main__':
    main()
