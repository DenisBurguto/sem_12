# Задание No1
# 📌 Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# 📌 Экземпляр должен запоминать последние k значений.
# 📌 Параметр k передаётся при создании экземпляра.
# 📌 Добавьте метод для просмотра ранее вызываемых значений и их факториалов.
from collections import OrderedDict


class Factorial:
    def __init__(self, k: int):
        self._k = k
        self._storage = OrderedDict()

    def __call__(self, number: int):
        if number not in self._storage:
            result = 1
            for i in range(1, number + 1):
                result *= i
                if len(self._storage) <= self._k:
                    self._storage[number] = result
                else:
                    self._storage.popitem(last=False)
                    self._storage[number] = result
            return result
        return self._storage[number]

    def get_previous_value(self, res=''):
        for num, fact in self._storage.items():
            res += ''.join(f'called_num = {num} and factorial = {fact} \n')
        print(res)
        return res


if __name__ == '__main__':
    # Создание экземпляра класса
    factorial = Factorial(5)

    # Вывод результата
    print(factorial(5))
    print(factorial(8))
    print(factorial(9))
    print(factorial(12))
    print(factorial(14))
    print(factorial(11))
    print(factorial(8))

    factorial.get_previous_value()
