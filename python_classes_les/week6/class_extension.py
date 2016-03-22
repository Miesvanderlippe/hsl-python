from shapes import Rectangle, Square, Circle


def main()->None:
    shape1 = Rectangle(100, 200)
    shape2 = Square(100)
    shape3 = Circle(100)

    print('Shape1 surface: {}'.format(shape1.surface))
    print('Shape1 perimiter: {}'.format(shape1.perimeter))

    print('Shape2 surface: {}'.format(shape2.surface))
    print('Shape2 perimiter: {}'.format(shape2.perimeter))

    print('Shape3 surface: {}'.format(shape3.surface))
    print('Shape3 perimiter: {}'.format(shape3.perimeter))

if __name__ == '__main__':
    main()
