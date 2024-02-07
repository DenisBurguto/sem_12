# Задание No4
# 📌 Доработайте класс прямоугольник из прошлых семинаров.
# 📌 Добавьте возможность изменять длину и ширину прямоугольника и
# встройте контроль недопустимых значений (отрицательных).
# 📌 Используйте декораторы свойств.
from typing import Union


class Rectangle:
    def __init__(self, length, width=None):
        self._length = length
        if width:
            self._width = width
        else:
            self._width = length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not isinstance(value, Union[int, float]):
            raise TypeError
        if value < 0:
            raise ValueError
        self._length = value


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, Union[int, float]):
            raise TypeError
        if value < 0:
            raise ValueError
        self._width = value

    def get_perimeter(self):
        return 2 * self._width + 2 * self._length

    def get_square(self):
        return self._width * self._length

    def __str__(self):
        return f'Rectangle(length = {self._length}, width = {self._width})'

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        new_length = self._length + other._length
        new_width = self._width + other._width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        new_length = self._length - other._length

        new_width = self._width - other._width
        if new_width >= 0 and new_length >= 0:
            return Rectangle(new_length, new_width)
        raise AttributeError('you subtract below zero')


if __name__ == '__main__':
    first = Rectangle(52, 10)
    second = Rectangle(5)
    print(first.get_perimeter())
    print(first.get_square())
    print(second.get_perimeter())
    print(second.get_square())
    print(first + second)
    print(first - second)

    first.length = 10
    print(first)
    first.width = 11.2
    print(first.__dict__)
