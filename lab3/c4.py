class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def move(self):
        self.x , self.y = [int(n) for n in input().split()]


    def dist(self):
        x1 = self.x
        y1 = self.y
        x2, y2 = [int(n) for n in input().split()]
        d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1 / 2
        print(d)

a = Point(1, 2)
a.show()
a.move()
a.dist()