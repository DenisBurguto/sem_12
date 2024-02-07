# Задание No3
# 📌 Создайте класс-генератор.
# 📌 Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# 📌 Если переданы два параметра, считаем step=1.
# 📌 Если передан один параметр, также считаем start=1.


class MyFactorialGenerator:
    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self._start = start
        self._stop = stop
        if self._start > self._stop:
            self._start, self._stop = self._stop, self._start
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        while self._start < self._stop:
            result = 1
            for i in range(1, self._start + 1):
                result *= i
            self._start += self._step
            return result
        raise StopIteration


if __name__ == '__main__':
    example = MyFactorialGenerator(20, step=4)
    for data in example:
        print(data)
