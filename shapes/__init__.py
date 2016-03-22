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


class Square:

    width = int
    height = int

    def __init__(self, width: int)->None:
        self.width = width
        self.height = width

    @property
    def perimeter(self)->int:
        return (self.height * 2) + (self.width * 2)

    @property
    def surface(self)->int:
        return self.height * self.width


class Circle:

    radius = int

    def __init__(self, radius: int)->None:
        self.radius = radius

    @property
    def perimeter(self)->int:
        return self.radius * pi * 2

    @property
    def surface(self)->int:
        return (self.radius * self.radius) * pi