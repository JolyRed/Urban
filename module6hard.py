import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = []

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def __is_valid_sides(self, *sides):
        return all(isinstance(x, int) and x > 0 for x in sides) and len(sides) == self.sides_count

    def get_color(self):
        return list(self.__color)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__height = self.__calc_height()

    def __calc_height(self):
        p = sum(self.__sides) / 2
        return (2 * ((p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2])) / self.__sides[0]) ** 0.5

    @property
    def height(self):
        return self.__height

    def get_square(self):
        return 0.5 * self.height * sum(self.__sides)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, side, *[side] * (self.sides_count - 1))

    def get_volume(self):
        return self.__sides[0] ** 3
