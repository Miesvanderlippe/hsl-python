from os import path, linesep
from random import choice
from time import time
from string import ascii_lowercase

__author__ = 'Mies van der Lippe'

# <editor-fold desc="Hangman art">
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
# </editor-fold>


class File:

    def __init__(self, file_path: str)->None:
        self.path = file_path

    # return lines in file
    def get_lines(self):
        with open(self.path, 'r') as f:
            return f.read().splitlines()

    # overwrite file with lines
    def save(self, lines: list)->None:
        with open(self.path, 'w') as f:
            return f.write(linesep.join(lines))

    # returns if a file exists
    def exists(self)->bool:
        return path.isfile(self.path)

    # append lines by using a list
    def append_lines(self)->None:
        raise NotImplementedError

    # append text to file
    def append_text(self)->None:
        raise NotImplementedError


class WordList:

    def __init__(self, file_path: str)->None:

        self.file = File(file_path)

        if not self.file.exists():
            raise FileNotFoundError('Kon de woordenlijst niet vinden. Sla deze '
                                    'op als {}'.format(file_path))

        self.word_list = self.file.get_lines()
        self.word_list = strip_empty_rows(self.word_list)

    # saves the word list
    def save(self)->None:
        self.file.save(self.word_list)

    # returns the entire list
    def get_word_list(self)->list:
        return self.word_list

    # get a random word from the word list
    def get_random_word(self)->str:
        return choice(self.word_list)

    # sort the word list
    def sort_word_list(self)->None:
        self.word_list.sort(key=lambda item: (len(item), item))

    # returns if an item is in the list already
    def in_list(self, word: str)->bool:
        return word in self.word_list

    # Add a file to the word list (saves it too)
    def add(self, word: str)->bool:
        if word not in self.word_list:
            self.word_list.append(word)
            self.sort_word_list()
            return True
        else:
            return False


class Highscores:

    headers = list
    scores = list

    def __init__(self, file_path: str)->None:
        self.file = File(file_path)

        if not self.load_scores_from_file():
            self.headers = self.default_headers()
            self.scores = self.default_scores()

    # loads scores from file
    def load_scores_from_file(self):

        if not self.file.exists():
            return False

        try:
            scores_in_file = strip_empty_rows(self.file.get_lines())
            scores = [x.split(';') for x in scores_in_file]
        except ValueError:
            return False
        else:
            self.headers = scores[0]  # headers are found on first row
            self.scores = scores[1::]  # scores follow

            # filter rows with missing information
            self.scores = [
                    row for row in self.scores
                    if type(row) == list and len(row) == 6
                ]

            # strip position indicator (not used)
            self.scores = [x[1::] for x in self.scores]

            # use default headers if missing or extra
            if not (len(self.headers) == 6 and type(self.headers) == list):
                self.headers = self.default_headers()

            return True

    def would_be_highscore(self, score: int)->bool:

        if len(self.scores) < 10:
            return True

        else:  # no else needed but whatever.
            lowest_score = self.scores[-1]

            return int(lowest_score[3]) < score

    # sort scores, trim to 10
    def sort_scores(self)->None:
        self.scores.sort(key=lambda item: (int(item[4]), item))
        self.scores.reverse()
        self.scores = self.scores[0:10]

    # add a score to scores
    def add_score(self, name: str, length: int, mistakes: int, seconds: int,
                  score: int):
        name = ''.join(name[0:20])
        self.scores.append(
                [name, str(length), str(mistakes), str(seconds), str(score)]
        )
        self.sort_scores()

    # save scores
    def save(self)->None:

        # list with positions (only make positions for scores we have
        tmp_scores = [[x] for x in range(1, len(self.scores)+1)]
        position = 1

        self.sort_scores()

        # extend positions with other info
        for score in self.scores:
            tmp_scores[position-1].extend(score)
            position += 1

        # insert headers
        tmp_scores.insert(0, self.headers)

        # incompetent join function is incompetent (can't join ints)
        tmp_scores = [[str(item) for item in row] for row in tmp_scores]

        self.file.save([';'.join(x) for x in tmp_scores])

    # printable highscores
    def printable_highscores(self)->str:

        position = 0

        string = '{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}\n'.format(
                self.headers[0], self.headers[1], self.headers[2],
                self.headers[3], self.headers[4], self.headers[5]
        )

        for scores in self.scores:
            position += 1
            string += '{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}\n'.format(
                    position, scores[0], scores[1], scores[2],
                    minutes_seconds(int(scores[3])), scores[4]
            )

        return string

    @staticmethod
    def calculate_score(time_elapsed: int, word: str, used_tries: int)->int:
        return int(
                round(10000 * (len(word) / ((time_elapsed * used_tries) + 1)))
        )

    # default headers
    @staticmethod
    def default_headers()->list:
        return ['Positie', 'Naam', 'Lengte', 'Fouten', 'Tijd', 'Score']

    # set of default scores
    @staticmethod
    def default_scores(amount: int = 10)->list:
        scores = []
        for x in range(1, amount + 1):
            scores.append([x, '<leeg>', 0, 0, 0, 0])

        return scores


class Hangman:

    def __init__(self, word: str):
        self.word_to_guess = word
        self.tries_used = 0
        self.guessed_letters = set()
        self.allowed_chars = ascii_lowercase

    def guess_letter(self, guess: str)->bool:
        guess = guess.lower()

        if guess not in self.allowed_chars:
            return False
        else:
            self.guessed_letters.add(guess)

        if guess in self.word_to_guess:
            return True
        else:
            self.tries_used += 1
            return False

    def player_alive(self)->bool:
        return self.tries_used < 9

    def won(self)->bool:
        for letter in self.word_to_guess:
            if letter not in self.guessed_letters:
                return False
        return True

    def guess_word(self, guess: str)->bool:
        guess = guess.lower()
        if guess == self.word_to_guess:
            self.guessed_letters.update([char for char in guess])
            return True

        else:
            if self.tries_used > 6:
                self.tries_used = 9
            else:
                self.tries_used += 3
            return False

    def guessed_letter_box(self)->list:

        stars_letters = ['*' if x not in sorted(self.guessed_letters) else x
                         for x in self.allowed_chars]
        chunks = array_chunk(stars_letters, 9)
        chunks = [' '.join(x) for x in chunks]

        return chunks

    def guesses_in_word(self):

        return ' '.join(
                [
                    '*' if x not in self.guessed_letters else x
                    for x in self.word_to_guess
                ])

    def main_interface(self)->str:

        letterbox = self.guessed_letter_box()

        return '{:>5}{:^60}\r\n' \
               '{:>5}{:^60}\r\n' \
               '{:>5}{:^60}\r\n' \
               '{:>5}\r\n' \
               '{:>5}\r\n' \
               '{:>5}\r\n' \
               '' \
               '{:^40}'.format(
                hangman[self.tries_used][0], letterbox[0],
                hangman[self.tries_used][1], letterbox[1],
                hangman[self.tries_used][2], letterbox[2],
                hangman[self.tries_used][3],
                hangman[self.tries_used][4],
                hangman[self.tries_used][5],
                self.guesses_in_word())

# <editor-fold desc="Standalone functions">


def minutes_seconds(seconds: int)->str:
    m, s = divmod(seconds, 60)
    return '{}m{}s'.format(m, s)


def strip_empty_rows(subject: list)->list:
        return [x for x in subject if len(x) > 0]


def longest_item_in_list_list(subject: list, key: int):
    length_longest_item = 0

    for item in subject:
        if len(item[key]) > length_longest_item:
            length_longest_item = len(item[key])

    return length_longest_item


def strip_nonalpha(word: str)->str:
    return ''.join([i for i in word if i.isalpha()]).lower()


def array_chunk(to_chunk: list, size: int)->list:
    return [
        to_chunk[offset:offset+size] for offset in range(0, len(to_chunk), size)
        ]
# </editor-fold>


def main()->None:

    # word list
    word_list_path = 'wordlist.txt'
    highscores_path = 'highscores.txt'

    wordlist = WordList(word_list_path)
    highscores = Highscores(highscores_path)

    name = ''

    while len(name) == 0:
        name = strip_nonalpha(input('geef uw naam'))

    # main loop
    while True:

        # <editor-fold desc="Menu options & selection">
        selection = input('Selecteer een van de volgende opties:\n'
                          '1) Een woord toevoegen\n2) Het spel spelen\n'
                          '3) De ranking bekijken\n4) Stoppen\n')

        try:
            selection = int(selection)
        except ValueError:
            print('Geen geldige optie geselecteerd')
            continue

        if selection not in range(1, 5):
            print('Geen geldige optie geselecteerd')
            continue
        # </editor-fold>

        # <editor-fold desc="Add a word">
        if selection == 1:

            word_to_add = input('Geef het woord wat je toe wilt voegen')
            word_to_add = strip_nonalpha(word_to_add)

            if len(word_to_add) > 0:

                if wordlist.add(word_to_add):
                    print('Woord toegevoegd')
                    wordlist.save()

                else:
                    print('Het woord bestond al')

            else:
                print('Er is geen geldig woord gevonden')
        # </editor-fold>

        # <editor-fold desc="Main game">
        elif selection == 2:
            word = wordlist.get_random_word()
            game = Hangman(word)
            time_start = time()

            print(word)
            print(game.main_interface())

            while game.player_alive() and not game.won():
                player_input = ''

                while len(player_input) == 0:
                    player_input = strip_nonalpha(
                            input('Geef een letter of raad het woord\n')
                        )

                if len(player_input) > 1:
                    game.guess_word(player_input)

                else:
                    game.guess_letter(player_input)

                print(game.main_interface())

            if game.won():
                print('U heeft gewonnen!')
                time_end = time()
                duration_sec = int(round(time_end-time_start))  # round != int?
                score = highscores.calculate_score(duration_sec, word,
                                                   game.tries_used)

                if highscores.would_be_highscore(score):

                    print('U heeft een highscore behaalt!')
                    highscores.add_score(name, len(word), game.tries_used,
                                         duration_sec, score)
                    highscores.save()
            else:
                print('Helaas u bent overleden!')
        # </editor-fold>

        # <editor-fold desc="View highscores">
        elif selection == 3:
            print(highscores.printable_highscores())
        # </editor-fold>

        # <editor-fold desc="Exit program">
        elif selection == 4:
            print('Het spel wordt afgesloten')
            exit()
        # </editor-fold>

        # just so I can fold my last region
        pass


if __name__ == '__main__':
    main()
