from random import shuffle

__author__ = 'Mies'


def draw(participants: list)->dict:

    # shuffle
    shuffle(participants)

    # create empty dict
    results = {x: '' for x in participants}

    # first person gets last person
    results[participants[0]] = participants[len(participants)-1]

    # second - last person gets the person in before them
    for i in range(1, len(participants)):
        results[participants[i]] = participants[i-1]

    return results


def main()-> None:

    res = draw(['A', 'B', 'C', 'D', 'E'])

    for i in res:
        print(i, res[i])


if __name__ == '__main__':
    main()