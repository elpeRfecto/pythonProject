class Rechtangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return f'(Координата x = {self.x}, Координата y = {self.y},' \
               f' Ширина прямоугольника = {self.width}, Высота прямоугольника = {self.height})'

rectan = Rechtangle(5, 10, 100, 50)

print(rectan.get_area())

