from random import randint


class Dice:

    _sides = int

    def __int__(self):
        self.sides = 6
        self.total = 0

    def roll(self):
        roll = randint(0, self.sides)
        self.total += roll
        return roll

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, value):

        if value % 2 > 0 or 2 < value > 20:
            value = 6

        self._sides = value


def main():

    dices = [
        Dice(),
        Dice(),
        Dice()
    ]


if __name__ == '__main__':
    main()