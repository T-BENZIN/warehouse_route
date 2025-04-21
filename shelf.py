def is_odd(number: int) -> bool:
    return bool(number % 2)


class Shelf:
    """Класс определяющий полку и рассчитывающий её свойства"""
    def __init__(self, address: str):
        """
        Инициализация экземпляра объекта.
        По введённому адресу полки рассчитываются координаты подбора с полки и координаты проходов к другим рядам.
        :param address: Адрес полки в текстовом формате. Например: 2/D/23
        :type address: str
        """
        self.__address = address.rsplit(sep='\n', maxsplit=1)[0]
        address_list = address.split(sep='/', maxsplit=2)
        self.__aisle = int(address_list[0])
        self.__shelf = address_list[1]
        self.__rack = int(address_list[2])
        self.__coordinates = self.coordinates_calculation()
        self.__pickup_coordinates = self.pickup_coordinates_calculation()
        self.__upper_passage_y_coordinate, self.__lower_passage_y_coordinate = self.passage_y_coordinates_calculation()

    @property
    def address(self) -> str:
        return self.__address

    @property
    def aisle(self) -> int:
        return self.__aisle

    @property
    def shelf(self) -> str:
        return self.__shelf

    @property
    def rack(self) -> int:
        return self.__rack

    @property
    def coordinates(self) -> tuple[int, int]:
        return self.__coordinates

    @property
    def pickup_coordinates(self) -> tuple[int, int]:
        return self.__pickup_coordinates

    @property
    def upper_passage_y_coordinate(self) -> int:
        return self.__upper_passage_y_coordinate

    @property
    def lower_passage_y_coordinate(self) -> int:
        return self.__lower_passage_y_coordinate

    def coordinates_calculation(self) -> tuple[int, int]:
        """Расчёт координат стеллажа"""
        if is_odd(self.aisle):
            x = (self.aisle // 2) * 3 + 2 if self.aisle > 1 else 2
        else:
            x = (self.aisle // 2) * 3 if self.aisle > 0 else 0
        if self.aisle < 5:
            y = self.rack if self.rack < 16 else self.rack + 1
        else:
            y = self.rack + 7
        return x, y

    def pickup_coordinates_calculation(self) -> tuple[int, int]:
        """Расчёт координат прилегающего прохода"""
        if is_odd(self.aisle):
            x = self.coordinates[0] - 1
        else:
            x = self.coordinates[0] + 1
        return x, self.coordinates[1]

    def passage_y_coordinates_calculation(self) -> tuple[int, int]:
        """Y-координаты проходов на параллельные ряды"""
        if self.aisle < 5:
            # upper = 0 if self.rack < 16 else 16
            # lower = 16 if self.rack < 16 else 28
            upper, lower = 0, 28
        else:
            upper, lower = 7, 28
        return upper, lower


if __name__ == '__main__':
    """Проверка работы класса Shelf на примере данных из input.txt"""
    order_list = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            shelf = Shelf(line)
            order_list.append(shelf)
            print(f'''
Полка {shelf.address} (ряд {shelf.aisle}, стеллаж {shelf.rack}, уровень {shelf.shelf})
расположена по координатам {shelf.coordinates} и место сборки на {shelf.pickup_coordinates}
ближайшие проходы на параллельные уровни находятся на Y: {shelf.upper_passage_y_coordinate} и {shelf.lower_passage_y_coordinate}''')
