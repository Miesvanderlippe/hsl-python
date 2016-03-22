
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


def main()->None:
    shape1 = Rectangle(100, 200)


if __name__ == '__main__':
    main()
