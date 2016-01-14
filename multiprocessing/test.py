from multiprocessing import Process
from time import sleep


def longtask()->None:
    sleep(2)
    print('x')


def main()->None:

    p0 = Process(target=longtask)
    p1 = Process(target=print, args=('ali',))
    p2 = Process(target=print, args=('bob',))
    p3 = Process(target=print, args=('calin',))
    p4 = Process(target=print, args=('dolan',))
    p5 = Process(target=print, args=('eduard',))

    p0.start()
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()

if __name__ == '__main__':
    main()