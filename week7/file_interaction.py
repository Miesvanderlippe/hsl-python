__author__ = 'Mies'


# a for append, r for read, w for write.
# file = open('tes2t.txt', 'w')

# file.write('Allahu Akbar')
# with file:
#    print(file.read())

# file.flush()
# file.close()


def main()-> None:

    name_list = []

    for i in range(0, 5):
        name_list.append(input('Voer naam {} in:\n'.format(i+1)))

    with open('namen.txt', 'w') as f:
        f.write('\r\n'.join(name_list))


    with open('namen.txt', 'r') as f:
        print(f.read())

if __name__ == '__main__':
    main()