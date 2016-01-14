import collections
from random import randint
from time import time


def main()-> None:

    t_start = time()

    # dictionary that counts
    throw_counter = collections.Counter()

    # length of counter changes with items in it, if it's 100 we must have every int between 1-100
    while len(throw_counter) < 100:

        # count throw (no need to save it elsewhere)
        throw_counter[str(randint(1, 100))] += 1

    # because sorting a dict or a counter doesn't work
    # could get keys from counter, sort keys and use those
    for i in range(1, 100):
        print('{}\tis {}\tx gegooid'.format(i, throw_counter[str(i)]))

    # unimportant stuff

    # get first item from most common items (key is side, value is amount thrown)
    side, amount = throw_counter.most_common()[0]

    # time elapsed = delta starting time, current time
    print('Time elapsed: {}'.format(time()-t_start))
    print('Most often thrown : {} which was thrown {} times'.format(side, amount))


if __name__ == '__main__':
    main()
