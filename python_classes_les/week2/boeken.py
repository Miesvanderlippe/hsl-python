from os import path


class File:

    def __init__(self, file_path: str)->None:
        self.path = file_path

    # return lines in file
    def get_lines(self)->list:
        """
        returns a list of lines in the file (w/o linebreaks)
        :return: Lines in file
        """
        with open(self.path, 'r') as f:
            return f.read().splitlines()

    # overwrite file with lines
    def save(self, lines: list)->None:
        """
        Save the list lines as lines to the file
        :param lines: list of lines to be saved
        :return: None
        """
        with open(self.path, 'w') as f:
            f.write('\n'.join(lines))

    # returns if a file exists
    def exists(self)->bool:
        """
        Returns whether file specified in constructor exists
        :return: Whether file exists
        """
        return path.isfile(self.path)


class Book:

    def __init__(self, title: str, writer: str, pages: int,
                 available: bool = True):
        self.title = title
        self.writer = writer
        self.available = available
        self.pages = pages
        self.code = self.gen_code()

    def __str__(self) -> str:
        return "Titel: {}\nAuteur: {}\nStatus: {}\nPagina's: {}\n".format(
                    self.title, self.writer,
                    {
                        True: "Beschikbaar",
                        False: "Niet beschrikbaar"
                    }[self.available],
                    self.pages
                )

    def set_title(self, new_title: str)->None:
        self.set_code(self.gen_code())  # gen new code because it's changed
        self.title = new_title

    def get_title(self)->str:
        return self.title

    def set_writer(self, new_writer: str)->None:
        self.set_code(self.gen_code())  # gen new code because it's changed
        self.writer = new_writer

    def get_writer(self)->str:
        return self.writer

    def set_available(self, new_state: bool)->None:
        self.available = new_state

    def get_available(self)->bool:
        return self.available

    def set_pages(self, new_pages: int)->None:
        self.pages = new_pages

    def get_pages(self)->int:
        return self.pages

    def get_code(self)->str:
        return self.code

    def set_code(self, new_code: str)->None:
        self.code = new_code

    def gen_code(self)->str:
        writer_last_name = self.writer.split(' ')
        writer_last_name = writer_last_name[-1]

        new_code = writer_last_name[0:2] + self.title[0:2]
        new_code = new_code.upper()

        return new_code


def main():

    library_file_path = 'boeken.txt'
    library_file = File( library_file_path)
    library = []

    if not library_file.exists():
        raise FileNotFoundError('Can\'t find specified dictionary file')

    library_lines = library_file.get_lines()

    for line in library_lines:
        title, writer, pages = line.split('|')
        library.append(Book(title, writer, int(pages)))

    total_pages = 0

    for book in library:
        total_pages += book.get_pages()

    average_pages = round(total_pages / len(library))
    print('Average amount of pages: {}'.format(average_pages))

if __name__ == '__main__':
    main()
