from random import randint


class Dice:

    _sides = int

    def __int__(self, sides: int = 6)->None:
        self.sides = sides
        self.total = 0

    def roll(self):
        roll = randint(0, self.sides)
        self.total += roll
        return roll

    @property
    def sides(self)->int:
        return self._sides

    @sides.setter
    def sides(self, value: int)->None:

        if value not in [2, 4, 6, 8, 10, 12, 20]:
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