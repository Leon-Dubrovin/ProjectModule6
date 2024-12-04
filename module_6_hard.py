import math

class Figure:
    sides_count = 0
    def __init__(self, color:tuple, *sides):
        self.__sides = [1] * self.sides_count
        self.set_sides(*sides)
        self.__color = None
        self.filled = False
        self.set_color(*color)
    def get_color(self):
        return self.__color
    def __is_valid_color(self, r, g, b):
        if (all(isinstance(channel, int) and channel <= 255 and channel >= 0 for channel in (r, g, b))):
            return True
        else:
            return False
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True
    def __is_valid_sides(self, *new_sides):
        if len(list(new_sides)) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides):
            return True
        else:
            return False
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return sum(self.__sides)
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
class Circle(Figure):
    sides_count = 1
    def __init__(self, color:tuple, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)
    def get_square(self):
        return (self.get_sides()[0] ** 2) / (4 * math.pi)
class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        sides = self.get_sides()
        p = sum(sides) / 2
        return (p * (p - sides[0]) * (p - sides()[1]) * (p - sides[2])) ** 0.5
class Cube(Figure):
    sides_count = 12
    def __init__(self, color:tuple, *sides):
        self.__sides = [1] * self.sides_count
        self.set_sides(*sides)
        self.filled = False
        self.set_color(*color)
    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], int) and new_sides[0] > 0:
            return True
        else:
            return False
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides) * self.sides_count
    def get_sides(self):
        return self.__sides
    def get_volume(self):
        return self.get_sides()[0] ** 3

if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    circle2 = Circle((300, 200, 100), 20)
    cube1 = Cube((222, 35, 130), 6)

    print('color:',circle2.get_color(), 'filled:', circle2.filled)
    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())