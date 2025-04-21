"""Создание списка со случайным набором ячеек для тестирования."""
from random import randint, choice


def random_cell() -> str:
    """Возвращает одну случайную ячейку реально существующую на складе Гаухар."""
    aisle = randint(0, 20)  # ряд
    rack = randint(1, 26) if aisle < 5 else randint(1, 20)  # секция
    shelf = choice('ABCDEF')  # полка
    address = f'{aisle}/{shelf}/{rack}'
    return address


if __name__ == '__main__':
    order_list = [random_cell() for _ in range(randint(10, 15))]
    with open('input.txt', 'w') as file:
        for item in order_list:
            file.writelines(f'{item}\n')
