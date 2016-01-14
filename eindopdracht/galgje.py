from os import path, linesep
from random import choice
import math
from time import time
from multiprocessing import Process

__author__ = 'Mies van der Lippe'

hangman = [
    ['          ', '          ', '          ',
     '          ', '          ', '          '],
    ['          ', '  |       ', '  |       ',
     '  |       ', '  |       ', ' / \      '],
    ['   ____   ', '  |/      ', '  |       ',
     '  |       ', '  |       ', ' / \      '],
    ['   ____   ', '  |/   |  ', '  |       ',
     '  |       ', '  |       ', ' / \      '],
    ['   ____   ', '  |/   |  ', '  |    O  ',
     '  |       ', '  |       ', ' / \      '],
    ['   ____   ', '  |/   |  ', '  |    O  ',
     '  |    |  ', '  |       ', ' / \      '],
    ['   ____   ', '  |/   |  ', '  |   \O  ',
     '  |    |  ', '  |       ', ' / \      '],
    ['   ____   ', '  |/   |  ', '  |   \O/ ',
     '  |    |  ', '  |       ', ' / \      '],
    ['   ____   ', '  |/   |  ', '  |   \O/ ',
     '  |    |  ', '  |   /   ', ' / \      '],
    ['   ____   ', '  |/   |  ', '  |   \O/ ',
     '  |    |  ', '  |   / \ ', ' / \      ']
]


def save_lines_to_file(file_path: str, lines: list)->bool:
    with open(file_path, 'w') as f:
        f.write(linesep.join(lines))


def strip_empty_rows(subject: list)->list:
    return [x for x in subject if len(x) > 0]


def get_lines_from_file(file_path: str)->list:
    with open(file_path, 'r') as f:
        return f.read().splitlines()


def file_exists(file_path: str)->bool:
    return path.isfile(file_path)


def get_word_list(file_path: str)->list:
    return [x for x in get_lines_from_file(file_path) if x]


def get_random_item_from_list(item_list: list)->str:
    return choice(item_list)


def guess_in_word(word: str, guess: str)->bool:
    return guess in word


def join_with_padding(to_join: list, pad_left: str, pad_right: str):
    return pad_left + (pad_right+pad_left).join(to_join) + pad_right


def longest_item_in_list_list(subject: list, key: int):
    length_longest_item = 0

    for item in subject:
        if len(item[key]) > length_longest_item:
            length_longest_item = len(item[key])

    return length_longest_item


def guessed_letters_in_word(word: str, guessed_letters: set,
                            unknown: str='*', pad_left: str='[',
                            pad_right: str=']')->str:

    guess_or_unkwn = [unknown if x not in guessed_letters else x for x in word]

    return join_with_padding(guess_or_unkwn, pad_left, pad_right)


def array_chunk(to_chunk: list, size: int)->list:
    return [to_chunk[x:x+size] for x in range(0, len(to_chunk), size)]


def guessed_letters_box(guessed_letters: set)->list:
    abc         = 'abcdefghijklmnopqrstuvwxyz'
    stars_letters = ['*' if x not in sorted(guessed_letters)
                     else x for x in abc]
    chunks = array_chunk(stars_letters, 9)
    chunks = [' '.join(x) for x in chunks]
    box_width = 19
    chunks.insert(0, 'Gebruikte letters')
    lines = []

    for chunk in chunks:
        padding_left  = ' ' * math.ceil((box_width-len(chunk))/2)
        padding_right = ' ' * math.floor((box_width-len(chunk))/2)
        lines.append(padding_left+chunk+padding_right)

    lines.insert(2, '')
    lines.insert(4, '')

    return lines


def fill_to_longest_row(to_fill: list, filling: str=' '):
    longest = len(max(to_fill, key=len))
    return [x+(filling*(longest-len(x))) for x in to_fill]


def box_it(to_box: list)->list:
    to_box = fill_to_longest_row(to_box)
    # return to_box
    width = len(to_box[0])
    to_box = ['║'+x+'║' for x in to_box]
    to_box.insert(0, '╔'+'═'*width+'╗')
    to_box.append('╚'+'═'*width+'╝')
    return to_box


def pad_it(to_pad: list, pad_vert: bool=True, padding: str=' '):
    to_pad = fill_to_longest_row(to_pad)
    longest = len(to_pad[0])
    if pad_vert:
        to_pad.insert(0, padding*longest)
        to_pad.append(padding*longest)
    return [' '+row+' ' for row in to_pad]


def iod(value: str, index: int, default: str='')->str:
    # index or default
    try:
        return value[index]
    except IndexError:
        return default


def calc_score(time_elapsed, word, used_tries: int)->int:
    return int(round(10000 * (len(word) / ((time_elapsed * used_tries) + 1))))


def get_highscores(path: str)->list:
    lines = strip_empty_rows(get_lines_from_file(path))
    scores = [x.split('|') for x in lines]
    scores = sort_highscores(scores)

    if len(scores) == 0:
        scores = [['default', 0] for x in range(0,10)]

    return scores


def write_highscores(scores: list, path: str)->bool:
    scores = sort_highscores(scores)
    scores = [x[0]+'|'+str(x[1]) for x in scores]
    return save_lines_to_file(path, scores)


def sort_highscores(scores: list)->list:
    scores.sort(key=lambda item: (int(item[1]), item))
    scores = scores[-10:]
    return scores


def printable_main_game_output(guessed_letters: list, incorrect: int,
                               word: str):
    global hangman
    d_hangman  = hangman[incorrect]
    d_guessed  = guessed_letters_box(guessed_letters)
    d_word     = [guessed_letters_in_word(word, guessed_letters, '*', ' ', '')]
    lines      = []
    longest_line = 0

    for i in range(0, 10):
        whitespace = ' ' * (50 - len(iod(d_hangman, i)))
        line = (iod(d_hangman, i) + whitespace + iod(d_guessed, i))
        if len(line) > longest_line:
            longest_line = len(line)
        lines.append(line)

    whitespace = ' ' * math.floor((longest_line - len(d_word[0]))/2)
    for line in d_word:
        lines.append(whitespace+line)

    return '\r\n'.join(pad_it(lines, False))


def printable_highscores(scores: list)->str:
    pad_to = longest_item_in_list_list(scores, 0) + 3
    print(pad_to)
    printable = []

    for score in scores[::-1]:
        printable.append('{} : {}'.format(score[0]+('-'*(pad_to-len(score[0]))), score[1]))

    return linesep.join(printable)


def strip_nonalpha(word: str)->str:
    return ''.join([i for i in word if i.isalpha()]).lower()


def main()->None:

    word_list_path   = 'wordlist.txt'
    word_list        = get_word_list(word_list_path)
    highscore_list_path = 'highscores.txt'
    highscore_list   = get_highscores(highscore_list_path)
    name             = input('Voer je naam in:\r\n')

    while name == '':
        name = input('Geen naam gevonden, probeer het opnieuw\r\n')

    while True:
        print('Selecteer een van de volgende opties:\r\n1) Een woord toevoegen'
              '\r\n2) Het spel spelen\r\n3) De ranking bekijken\r\n4) Stoppen')

        selection = input('')

        try:
            selection = int(selection)
        except ValueError:
            print('Geen geldige optie geselecteerd')
            continue

        if selection not in range(1, 5):
            print('Geen geldige optie geselecteerd')
            continue

        if selection == 4:
            print('Het spel word afgesloten')
            exit()

        if selection == 3:
            print(printable_highscores(highscore_list))

        if selection == 2:

            guessed_letters  = set()
            incorrect        = 0
            time_start       = time()
            correct          = False
            word             = get_random_item_from_list(word_list)
            letters_to_guess = word
            score            = 0

            # print(word)

            while True:

                print(printable_main_game_output(guessed_letters, incorrect,
                                                 word))

                if len(letters_to_guess) == 0:
                    correct = True
                    break

                if incorrect > 8:
                    print('Game over')
                    break

                guess = strip_nonalpha(input('Geef een letter of raad het woord in een keer\n\r').lower())

                if len(guess) == 0:
                    print('Geen (geldige) karakters gevonden')
                    continue

                elif len(guess) == 1:
                    if guess in guessed_letters:
                        print('Deze letter heb je al geraden')
                        continue
                    else:
                        guessed_letters.add(guess)
                        if guess_in_word(word, guess):
                            letters_to_guess = letters_to_guess.replace(guess,
                                                                        '')
                            continue
                        else:
                            incorrect += 1
                            continue

                else:
                    if guess == word:
                        correct = True
                        break
                    else:
                        print('Woord niet geraden, +3 pogingen')
                        incorrect += 3
                        continue

            time_end = time()
            duration_sec = round(time_end-time_start)
            score = calc_score(duration_sec, word, incorrect)

            print('Je heb het woord {} geraden. \r\nJe heb er {} seconde(n) '
                  'over gedaan\r\n'.format(['niet',
                                            ''][correct], duration_sec))
            print('Het woord was: {}'.format(word))
            print('{}, je score is:{}'.format(name, score))

            if int(round(score)) > int(highscore_list[0][1]) and correct:
                print('Gefeliciteerd! Je heb een nieuwe highscore behaald')
                highscore_list.append([name, score])
                highscore_list = sort_highscores(highscore_list)
                Process(target=write_highscores, args=(highscore_list, highscore_list_path)).start()

        if selection == 1:

            stop_loop = False

            while True:
                if stop_loop:
                    break

                word = strip_nonalpha(input('Geef het woord op (alleen letters'
                                            ' in het normale alfabet)\r\n'))
                if len(word) == 0:
                    print('Woord is niet lang genoeg')

                elif word in word_list:
                    print('Woord bestaat al in de lijst')

                else:
                    word_list.append(word)
                    word_list.sort(key=lambda item: (len(item), item))
                    Process(target=save_lines_to_file, args=(word_list_path, word_list)).start()

                    print('Woord toegevoegd')
                    break

                while True:

                    ans = input('Nogmaals proberen?\r\n').lower()
                    if ans in ['ja', 'yes', 'j', 'y']:
                        break

                    elif ans in ['nee', 'no', 'n']:
                        stop_loop = True
                        break


if __name__ == '__main__':
    main()

