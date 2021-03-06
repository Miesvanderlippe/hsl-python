from os import path
from random import choice
from time import time
from string import ascii_lowercase
import re

__author__ = 'Mies van der Lippe'

"""
student : Mies van der Lippe
studentnummer : s1096607
vak : binp periode 1
opdracht : eindopdracht galgje
klas : bin1e
"""

# <editor-fold desc="Hangman art">
"""
ik kan een bestand lezen, een split uitvoeren en een list list gebruiken
zie hiervoor de highscores. Het galgje karakter uit een betsand lezen
heeft geen toegevoegde waare
"""
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
    def get_lines(self)->list:
        """
        returns a list of lines in the file (w/o linebreaks)
        :return: Lines in file
        """
        with open(self.path, 'r') as f:
            return f.read().splitlines()

    # overwrite file with lines
    def save(self, lines: list)->None:
        """
        Save the list lines as lines to the file
        :param lines: list of lines to be saved
        :return: None
        """
        with open(self.path, 'w') as f:
            f.write('\n'.join(lines))

    # returns if a file exists
    def exists(self)->bool:
        """
        Returns whether file specified in constructor exists
        :return: Whether file exists
        """
        return path.isfile(self.path)

    # append lines by using a list
    def append_lines(self)->None:
        """
        Appends lines in list to the file NOT IMPLEMENTED
        """
        raise NotImplementedError

    # append text to file
    def append_text(self)->None:
        """
        Appends raw texts to the file NOT IMPLEMENTED
        """
        raise NotImplementedError


class WordList:

    def __init__(self, file_path: str)->None:

        self.file = File(file_path)

        if not self.file.exists():
            raise FileNotFoundError('Kon de woordenlijst niet vinden. Sla'
                                    ' deze op als {}'.format(file_path))

        self.word_list = self.file.get_lines()
        self.word_list = strip_empty_rows(self.word_list)

    # saves the word list
    def save(self)->None:
        """
        Save the wordlist
        """
        self.file.save(self.word_list)

    # returns the entire list
    def get_word_list(self)->list:
        """
        Return the wordlist as a list
        :return: The wordlist
        """
        return self.word_list

    # get a random word from the word list
    def get_random_word(self)->str:
        """
        Returns a random word from the wordlist using random.choice
        :return: A random word from wordlist
        """
        return choice(self.word_list)

    # sort the word list
    def sort_word_list(self)->None:
        """
        Sorts the wordlist as specified in instructions
        """
        self.word_list.sort(key=lambda item: (len(item), item))

    # returns if an item is in the list already
    def in_list(self, word: str)->bool:
        """
        Checks if a word already exists in the wordlist
        :param word: Word to check
        :return: Whether word exists in wordlist
        """
        return word in self.word_list

    # Add a file to the word list (saves it too)
    def add(self, word: str)->bool:
        """
        Add a word to the wordlist
        :param word: Word to add
        :return: Whether addition was successful
        """
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
    def load_scores_from_file(self)->bool:

        """
        Triest to load scores from the file also filtering all scores
        and the headers
        :return: Whether loading was successful. Results are saved to self.
        """
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

            self.scores = [
                    row for row in self.scores
                    if row[2].isdigit() and
                    row[3].isdigit() and
                    row[4].isdigit() and
                    row[5].isdigit()
                ]

            # strip position indicator (not used)
            self.scores = [x[1::] for x in self.scores]

            # use default headers if missing or extra
            if not (len(self.headers) == 6 and type(self.headers) == list):
                self.headers = self.default_headers()

            return True

    def would_get_position(self, score: int)->int:
        """
        Checks what position a score would get in the highscores
        :param score: Score to check
        :return: Position score would get. -1 if >position 10
        """
        if len(self.scores) == 0:
            return 1

        for position in range(0, len(self.scores)):
            if score > int(self.scores[position][4]):
                return position+1

        if len(self.scores) < 10:
            return len(self.scores)+1

        return -1

    def would_be_highscore(self, score: int)->bool:

        """
        Check whether a score would be a highscore
        (checks against lowest score)
        :param score: Score to check
        :return: Whether score would be in highscores
        """
        if len(self.scores) < 10:
            return True

        else:  # no else needed but whatever.
            lowest_score = self.scores[-1]

            return int(lowest_score[4]) < score

    # sort scores, trim to 10
    def sort_scores(self)->None:
        """
        Sorts the scores
        """
        self.scores.sort(key=lambda item: (int(item[4]), item), reverse=True)
        self.scores = self.scores[0:10]

    # add a score to scores
    def add_score(self, name: str, length: int, mistakes: int, seconds: int,
                  score: int)->None:
        """
        Add a score to the highscore list. List is then ordered & trimmed
        :param name: name of the player
        :param length: Length of the word
        :param mistakes: Mistakes made by player
        :param seconds: Time it took to guess the word ( in seconds)
        :param score: Calculated score
        """
        name = ''.join(name[0:20])
        self.scores.append(
                [name, str(length), str(mistakes), str(seconds), str(score)]
        )
        self.sort_scores()

    # save scores
    def save(self)->None:
        """
        Save the highscore list to file
        """

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
        """
        Gives a printable highscore table as a string w/ linebreaks
        :return:
        """
        position = 0
        tmp_scores = self.scores

        if len(tmp_scores) < 11:
            tmp_scores.extend(self.default_scores(10-len(self.scores)))

        string = '{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}\n'.format(
                self.headers[0], self.headers[1], self.headers[2],
                self.headers[3], self.headers[4], self.headers[5]
        )

        for scores in tmp_scores:
            position += 1
            string += '{:<10}{:<20}{:<10}{:<10}{:<10}{:<15}\n'.format(
                    position, scores[0], scores[1], scores[2],
                    minutes_seconds(int(scores[3])), scores[4]
            )

        return string

    @staticmethod
    def calculate_score(time_elapsed: int, word: str, faults: int)->int:
        """
        Calculates the score
        :param time_elapsed: Time it took to guess the word ( seconds)
        :param word: Word the player guessed
        :param faults: Amount of mistakes the player made
        :return: The score
        """
        return int(
                round(10000 * (len(word) / ((time_elapsed * faults) + 1)))
        )

    # default headers
    @staticmethod
    def default_headers()->list:
        """
        Default headers for the scoreboard
        :return: Default headers
        """
        return ['Positie', 'Naam', 'Lengte', 'Fouten', 'Tijd', 'Score']

    # set of default scores
    @staticmethod
    def default_scores(amount: int = 10)->list:
        """
        Default scores to be used to fill the scoreboard
        :param amount: Entries to be returned
        :return: List of placeholder scores
        """
        scores = []
        for x in range(1, amount + 1):
            scores.append(['<leeg>', 0, 0, 0, 0])

        return scores


class Hangman:

    def __init__(self, word: str):
        self.word_to_guess = word
        self.tries_used = 0
        self.guessed_letters = set()
        self.allowed_chars = ascii_lowercase
        self.word_set = set([x for x in word])

    def guess_letter(self, guess: str)->bool:
        """
        Guess a letter in the word
        :param guess: letter to guess
        :return: Whether guess was successful
        """
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
        """
        Check if the player still lives
        :return: Whether the player is alive
        """
        return self.tries_used < 9

    def won(self)->bool:
        """
        Check if the game has been won yet
        :return: Whether the game has been won
        """
        return self.word_set.issubset(self.guessed_letters)

    def guess_word(self, guess: str)->bool:
        """
        Guess the entire word. Also updates guessed letters if
        correct, lives when incorrect.
        :param guess: Word to guess
        :return: Whether the word was correct
        """
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
        """
        Returns the guessed letters in the alphabet, in 3 chunks.
        Letters that haven't been guessed are stars
        TODO:
        - kwarg for char instead of *
        - amount of chunks
        - Rename the function
        :return: List of 3 strings of guessed letters in alphabet
        """
        stars_letters = ['*' if x not in sorted(self.guessed_letters) else x
                         for x in self.allowed_chars]
        chunks = array_chunk(stars_letters, 9)
        chunks = [' '.join(x) for x in chunks]

        return chunks

    def guesses_in_word(self):
        """
        Returns the guessed letters in the word with not guessed
        letters blanked out by a *
        :return: word w/ not guessed letters blanked out
        """
        return ' '.join(
                [
                    '*' if x not in self.guessed_letters else x
                    for x in self.word_to_guess
                ])

    def main_interface(self)->str:
        """
        Directly printable game interface w/ guessed letters,
        blanked out word and gallow
        :return:
        """
        letterbox = self.guessed_letter_box()

        return '{:>5}{:>41}\n'\
               '{:>5}{:^60}\n' \
               '{:>5}\n' \
               '{:>5}{:^60}\n' \
               '{:>5}\n' \
               '{:>5}{:^60}\n' \
               '{:>5}\n' \
               '\n' \
               '{:^40}\n' \
               '{:^40}'.format(
                'Galgje:', 'Gebruikte letters',
                hangman[self.tries_used][0], letterbox[0],
                hangman[self.tries_used][1],
                hangman[self.tries_used][2], letterbox[1],
                hangman[self.tries_used][3],
                hangman[self.tries_used][4], letterbox[2],
                hangman[self.tries_used][5],
                'Het te raden woord:',
                self.guesses_in_word())

# <editor-fold desc="Standalone functions">


def minutes_seconds(seconds: int)->str:
    """
    amount of minutes and seconds in any amount of seconds
    TODO
    - Kwargs for m and s strings
    :param seconds: Amount of seconds to display
    :return: string with minutes and seconds
    """
    m, s = divmod(seconds, 60)
    return '{}m{}s'.format(m, s)


def strip_empty_rows(subject: list)->list:
    """
    Strips a list of it's empty items (len 0)
    :param subject: List to strip
    :return: Stripped list
    """
    return [x for x in subject if len(x) > 0]


def strip_nonalpha(word: str)->str:
    """
    Strip any non alphabetic character from a string
    :param word: String to strip
    :return: Stripped string
    """
    return re.sub('[^a-zA-Z]+', '', word)


def array_chunk(to_chunk: list, size: int)->list:
    """
    Divides an list into chunks. Last chunk will have
    any remaining items
    :param to_chunk: List to divide
    :param size: Length of each chunk
    :return: Chunks in a list
    """
    return [
        to_chunk[offset:offset+size]
        for offset in range(0, len(to_chunk), size)
        ]
# </editor-fold>


def main()->None:

    word_list_path = 'woorden.lst'
    highscores_path = 'rankings.txt'

    wordlist = WordList(word_list_path)
    highscores = Highscores(highscores_path)

    name = ''

    while len(name) == 0:
        # allow Uppercase letters in names
        name = strip_nonalpha(input('Wat is je naam?:\n'))

    # main loop
    while True:

        # <editor-fold desc="Menu options & selection">
        selection = input('1. Een woord toevoegen\n2. Het spel spelen\n'
                          '3. De ranking bekijken\n4. Stoppen\n\nWat wil je '
                          'doen? [1 - 4]')

        try:
            selection = int(selection)

        except ValueError:
            print('Dit is geen geldige invoer, probeer opnieuw!')
            continue

        if selection not in range(1, 5):
            print('Dit is geen geldige invoer, probeer opnieuw!')
            continue
        # </editor-fold>

        # <editor-fold desc="Add a word">
        if selection == 1:

            word_to_add = input('Voer een woord in die je wilt toevoegen aan '
                                'de woordenlijst:\n')
            word_to_add = strip_nonalpha(word_to_add)

            if 2 < len(word_to_add) < 39:

                if wordlist.add(word_to_add):
                    print('Het woord {} is toegevoegd aan de '
                          'woordenlijst!\n'.format(word_to_add))
                    wordlist.save()

                else:
                    print('Het woord {} staat al in de '
                          'woordenlijst!'.format(word_to_add))

            else:
                print('Het woord moet minstens 3 letters lang zijn en '
                      'maximaal 38 letters lang!')
        # </editor-fold>

        # <editor-fold desc="Main game">
        elif selection == 2:

            word = wordlist.get_random_word()
            game = Hangman(word)
            time_start = time()

            print(game.main_interface())

            while game.player_alive() and not game.won():

                player_input = ''

                while len(player_input) == 0:
                    player_input = strip_nonalpha(
                            input('Typ een letter of het woord:\n')
                        )

                    if len(player_input) == 0:
                        print('Dit is geen geldige invoer probeer opnieuw!')

                if len(player_input) > 1:
                    game.guess_word(player_input)

                else:
                    game.guess_letter(player_input)

                print(game.main_interface())

            if game.won():

                time_end = time()
                duration_sec = int(round(time_end-time_start))  # round != int?
                score = highscores.calculate_score(duration_sec, word,
                                                   game.tries_used)

                print('Je hebt het geraden! Het woord was {}\n\n'
                      'Je hebt {} punten gescoord\n'.format(word, score))

                if highscores.would_be_highscore(score):

                    position = highscores.would_get_position(score)
                    highscores.add_score(name, len(word), game.tries_used,
                                         duration_sec, score)
                    highscores.save()

                    print('Daarmee kom je op plaats {} in de '
                          'ranking!\n'.format(position))
                    print(highscores.printable_highscores())

            else:
                print('Helaas, je hebt het woord niet geraden. '
                      'Het woord was {}\n'.format(word))

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
