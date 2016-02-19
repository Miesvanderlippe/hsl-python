
class Book:

    def __init__(self, title: str, writer: str, available: bool, pages: int):
        self.title = title
        self.writer = writer
        self.available = available
        self.pages = pages
        self.code = ''

    def set_title(self, new_title: str)->None:
        self.title = new_title

    def get_title(self)->str:
        return self.title

    def set_writer(self, new_writer: str)->None:
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

    def gen_code(self)->None:
        raise NotImplementedError()


def main():
    pass

if __name__ == '__main__':
    main()
