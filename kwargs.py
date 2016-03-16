
def kwargs_test(normale_parameter, **kwargs)->None:
    print(kwargs)


def main()->None:
    kwargs_test('Parameter', keyword_argument='test')

if __name__ == '__main__':
    main()
