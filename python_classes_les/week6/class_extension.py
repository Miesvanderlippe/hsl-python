
class Rectangle:

    width = int
    height = int

    def __init__(self, width: int, height: int)->None:
        self.width = width
        self.height = height

    @property
    def perimeter(self)->int:
        return (self.height * 2) + (self.width * 2)

    @property
    def surface(self)->int:
        return self.height * self.width


class Square:

    width = int
    height = int

    def __init__(self, width: int)->None:
        self.width = width
        self.height = width

    @property
    def perimeter(self)->int:
        return (self.height * 2) + (self.width * 2)

    @property
    def surface(self)->int:
        return self.height * self.width


def main()->None:
    shape1 = Rectangle(100, 200)
    shape2 = Square(100)

    print('Shape1 surface: {}'.format(shape1.surface))
    print('Shape1 perimiter: {}'.format(shape1.perimeter))

    print('Shape2 surface: {}'.format(shape2.surface))
    print('Shape2 perimiter: {}'.format(shape2.perimeter))

if __name__ == '__main__':
    main()
