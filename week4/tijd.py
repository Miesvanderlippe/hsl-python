__author__ = 'Mies'

for uur in range(0, 24):
    for minute in range(0, 60):
        for second in range(0, 60):
            print('{:0>2}:{:0>2}:{:0>2}'.format(uur, minute, second))