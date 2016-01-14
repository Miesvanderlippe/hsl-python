
def kwargs(**kwargs)->None:
    print(kwargs)


def main()->None:
    kwargs(yolo='test')

if __name__ == '__main__':
    main()
