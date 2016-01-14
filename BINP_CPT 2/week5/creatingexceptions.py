
def main()->None:
    try:
        open('x.html')
    except FileNotFoundError:
        print('Yolo')
        raise

if __name__ == '__main__':
    main()