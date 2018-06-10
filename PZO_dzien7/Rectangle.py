""" Implementation of the Rectangle class"""

class Rectangle:
    """ A Rectangle.

    Args:
        width: width of the rectangle
        height: height of the rectangle
        Both width and height should be positive numbers
        """

    def __init__(self, width, height):
        if width <= 0:
            raise ValueError('Width must be positive.')
        if height <= 0:
            raise ValueError('Height must be positive.')
        self.width = width
        self.height = height

    def area(self):
        """Computes the area of the rectangle."""
        return self.height*self.width

    def perimeter(self):
        """Computes the perimeter of the rectangle."""
        return self.height*2+self.width*2
    def draw(self):
        """Draws the sketch of the rectangle."""
        pass

rect = Rectangle(100, 20)
print("wysokosc: ", rect.height)
print("szerokosc: ", rect.width)
print("pole powierzchni: ", rect.area())
print("Obwod: ", rect.perimeter())