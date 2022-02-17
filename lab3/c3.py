class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.s = 0

    def p_area(self):
        print(self.s)

class Rectangle(Shape):
    def area(self):
        self.s = self.length * self.width


a = Rectangle(5 , 7)
a.area()
a.p_area()