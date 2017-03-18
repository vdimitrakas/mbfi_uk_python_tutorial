from math import sqrt


class Rectangle:

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2*(self.width + self.length)

    def info(self):
        return 'Rectangle: (width: %d, length: %d)' % (self.width, self.length)

class Square(Rectangle):

    def __init__(self, length):
        self.length = length
        super().__init__(self.length, self.length)

    def info(self):
        return 'Square: (length: %d)' % self.length


if __name__ == '__main__':
    my_rectangle = Rectangle(2,3)
    print("The " + my_rectangle.info() + " has an area of %d and a perimeter of %d" % (my_rectangle.area(), my_rectangle.perimeter()))

    my_square = Square(8)
    print("The " + my_square.info() + " has an area of %d and a perimeter of %d" % (my_square.area(), my_square.perimeter()))