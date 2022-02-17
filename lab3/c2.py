class Shape:
    def __init__(self, length):
        self.length = length
        self.s = 0

    def p_area(self):
        print(self.s)



class Square(Shape):
    def area(self):
        self.s = self.length ** 2






a = Square(5)
a.area()
a.p_area()