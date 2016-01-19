from timeit import timeit
from string import ascii_lowercase
from string import ascii_letters
import re

ascii_lower_set = set([x for x in ascii_lowercase])
ascii_letters_set = set([x for x in ascii_letters])

subject = 'This%3Is1AS0ubjct14$%$%^insdvwith a l0tofCh@arcs'


def filter1(subject: str)->str:
    return ''.join([x for x in subject if x.isalpha()])


def filter2(subject: str)->str:
    return ''.join([x for x in subject if x.lower() in ascii_lowercase])


def filter3(subject: str)->str:
    return ''.join([x for x in subject if x in ascii_letters])


def filter4(subject: str)->str:
    return ''.join([x for x in subject if x in ascii_letters_set])


def filter5(subject: str)->str:
    return ''.join([x for x in subject if x.lower() in ascii_lower_set])


def filter6(subject: str)->str:
    return re.sub('[^a-zA-Z]+', '', subject)


def main()->None:
    print(filter6(subject))
    print('Long subject:\n'
      'filter 1{:>20}\n'
      'filter 2{:>20}\n'
      'filter 3{:>20}\n'
      'filter 4{:>20}\n'
      'filter 5{:>20}\n'
      'filter 6{:>20}\n'.format(
            timeit("filter1(subject)", setup="from __main__ import filter1, subject"),
            timeit("filter2(subject)", setup="from __main__ import filter2, subject"),
            timeit("filter3(subject)", setup="from __main__ import filter3, subject"),
            timeit("filter4(subject)", setup="from __main__ import filter4, subject"),
            timeit("filter5(subject)", setup="from __main__ import filter5, subject"),
            timeit("filter6(subject)", setup="import re; from __main__ import filter6, subject")
        ))





if __name__ == '__main__':
    main()