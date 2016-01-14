__author__ = 'Mies'

from os import path
from os import linesep

"""
7. Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the writ- ten portion of the
driver’s license exam. The exam has 20 multiple-choice questions. Here are the correct answers:
1.A 6.B 2.C 7.C 3.A 8.A 4.A 9.C 5.D 10.B
11. A 12. D 13. C 14. A 15. D
16. C 17. B 18. B 19. D 20. A
Your program should store these correct answers in a list. The program should read the student’s answers for each of the
20 questions from a text file and store the answers in another list. (Create your own text file to test the application
.) After the student’s answers have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions to pass the exam.) It should
then display the total number of correctly answered questions, the total number of incorrectly answered questions, and
a list showing the question numbers of the incorrectly answered questions.
"""

'''
Had beter met classjes gekunt :(
'''

VALID_ANSWERS = ['A', 'B', 'C', 'D']

# file functions


def file_exists(file_path: str)->bool:
    '''
    :param file_path: Path to file
    :return: Wether the file exists or not

    Checks if a file exists at the specified path
    '''
    return path.isfile(file_path)


def get_lines_from_file(file_path: str)->list:
    '''
    :param file_path: Path to file
    :return: List with rows of text with stripped ends

    Gets all text from a file, strips the ends of and puts them line by line in a list
    '''
    if file_exists(file_path):
        with open(file_path) as f:
            return [x.rstrip() for x in f.readlines()]

    return False


# string functions


def implode_to_string(lines: list, separator: str=' ')->str:
    '''
    :param lines: List containing items to be joined together
    :param separator: String to be put in between entries in list
    :return: String containing joined entries

    Joins list using a seperator
    '''
    return separator.join(map(str, lines))


def split_questions(questions: str)->list:
    '''
    :param questions: String containing questions
    :return: List containing question.answer
    '''
    return questions.split(' ')


def split_question_answer(line: str)->list:
    '''
    :param line: Question.answer
    :return: [question, answer]
    '''
    return line.split('.')

# question functions


def separated_questions_answers(lines: list)->list:
    '''
    :param lines: List of questions
    :return: List of split questions and answers
    '''
    return [split_question_answer(x) for x in lines]


def questions_answers_to_dictionary(questions: list)->dict:
    '''
    :param questions: List containing [question, answer] entries
    :return: Dictionairy containing question:answer (self sorts)
    '''
    return {int(question_no): question_answer for (question_no, question_answer) in questions}


# input functions


def file_path_input(msg: str="Please enter the file path.{}".format(linesep),
                   error_msg: str="Can't find the file specified. Please try again.{}".format(linesep))->str:
    '''
    :param msg: Question asked to user
    :param error_msg: Feedback if file can't be found
    :return: User-input filepath

    Gives error message and repeats question until valid filepath is entered
    '''
    while True:
        path = input(msg)

        if file_exists(path):
            return path
        else:
            print(error_msg)


def get_answer(question: str='Antwoord:{}'.format(linesep), invalid_mes: str='Geen geldig antwoord')->str:
    '''
    :param question: Question to be asked
    :param invalid_mes: Message to user when answer isn't considered valid (not a,b,c or d, or nothing at all)
    :return: the answer given

    Gives error message and repeats question until valid answer is entered
    '''
    answer = input(question)

    while answer.upper() not in VALID_ANSWERS:
        print(invalid_mes)
        answer = input(question)

    return answer.upper()


def main():
    # setup
    print('\033[95mExaminator:\033[0m')

    # get text from file
    file_path = file_path_input('Pad naar antwoordenblad:{}'.format(linesep), 'Het pad is ongeldig')
    lines = get_lines_from_file(file_path)

    # translate questions in file to usable format
    questions = split_questions(implode_to_string(lines))
    question_dictionary = questions_answers_to_dictionary(separated_questions_answers(questions))

    # ask questions
    print('\033[95mLeerling:\033[0m')

    score = 0
    incorrect = []

    for question, answer in question_dictionary.items():
        if answer == get_answer('Antwoord op vraag {}:{}'.format(question, linesep)):
            score += 1
        else:
            incorrect.append(question)

    # Give feedback
    print('U heeft het examen {}gehaald met een score van {}'.format(['', 'niet '][len(incorrect) > 5], score))

    if len(incorrect) > 0:
        print('Incorrect beantwoorde vragen :{} {}'.format(linesep, implode_to_string(incorrect,', ')))

if __name__ == "__main__":
    main()