# Задание No6
# 📌 Изменяем класс прямоугольника.
# 📌 Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
from typing import Union


class NotNegativeNumber(object):
    def __init__(self):
        self.min = 0

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f"You don't have permission to delete  {self.param_name}")

    def validate(self, value):
        if not isinstance(value, Union[int, float]):
            raise TypeError
        if value < self.min:
            raise ValueError


class Rectangle:
    length = NotNegativeNumber()
    width = NotNegativeNumber()

    def __init__(self, length, width=None):
        self.length = length
        if width:
            self.width = width
        else:
            self.width = length

    def get_perimeter(self):
        return 2 * self.width + 2 * self.length

    def get_square(self):
        return self.width * self.length

    def __str__(self):
        return f'Rectangle(length = {self.length}, width = {self.width})'

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        new_length = self.length - other.length

        new_width = self.width - other.width
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
    print(first)

