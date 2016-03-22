
class Square:

    width = int
    height = int

    def __init__(self, width: int, height: int)->None:
        self.width = width
        self.height = height

    @property
    def perimeter(self)->int:
        return (self.height * 2) + (self.width * 2)
