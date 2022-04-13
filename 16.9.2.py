class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def get_area(self):
        return self.length * self.width

rectangle = Rectangle(12, 24)

print('Площадь прямоугольника равна', rectangle.get_area())