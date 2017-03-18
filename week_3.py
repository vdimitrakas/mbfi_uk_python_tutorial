from math import sqrt
from random import randint

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
        super().__init__(length, length)

    def info(self):
        return 'Square: (length: %d)' % self.length


class Car:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add_x(self):
        self.x += 1

    def add_y(self):
        self.y += 1

    def move_car(self, x=5, y=10):
        self.x = x
        self.y = y

    def get_distance(a, b):
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def distance_from(self, b):
        return sqrt((self.x - b.x)**2 + (self.y - b.y)**2)

    def __str__(self):
        return 'Car location at: (%d, %d)' % (self.x, self.y)


class Racing(Car):

    def __init__(self, x, y):
        self.trips_made = 0
        super().__init__(x, y)

    def __str__(self):
        return 'Car location at: (%d, %d)' % (self.x, self.y)


def ex_3_1():
    my_rectangle = Rectangle(2, 3)

    print('Exercise 1')
    print("The " + my_rectangle.info() + " has an area of %d and a perimeter of %d" % (my_rectangle.area(), my_rectangle.perimeter()))

    my_square = Square(5)
    print("\nThe " + my_square.info() + " has an area of %d and a perimeter of %d" % (my_square.area(), my_square.perimeter()))


def ex_3_2():

    car = Car(randint(0, 100), randint(0, 100))
    for i in range(1, 11):
        racing = Racing(randint(0, 100), randint(0, 100))
        print('The car is %3.3f units away from racing car %d' % (Car.get_distance(car, racing), int(i)))
        # print('The car is %3.3f units away from racing car %d' % (car.distance_from(racing), int(i)))


if __name__ == '__main__':

    ex_3_1()
    print('\n\nExercise 2')
    ex_3_2()