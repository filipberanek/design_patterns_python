#LSP
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        self._height = value

def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = (int(w*10))
    print(f"Expected an area of {expected}, fot {rc.area}")

rc = Rectangle(2,3)
use_it(rc)