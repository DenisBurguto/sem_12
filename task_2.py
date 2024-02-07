# Задание No2
# 📌 Доработаем задачу 1.
# 📌 Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial.json', 'w', encoding='utf-8') as f:
            json.dump(self._storage, f, indent= 2)


if __name__ == '__main__':
    # Создание экземпляра класса

    factorial = Factorial(5)
    with factorial as f:
        f(12)
        f(8)
        f(9)
        print(f(12))
        f(14)
        f(11)
        f(8)
        print(f(14))

    factorial.get_previous_value()
    with open('factorial.json', 'r',) as f:
        print(json.load(f))
