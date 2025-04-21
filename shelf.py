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
        self.__address = address
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
        if is_odd(self.aisle):
            x = (self.aisle - 1) * 3 + 2
        else:
            x = (self.aisle - 1) * 3 if self.aisle > 0 else 0
        if self.aisle < 5:
            y = self.rack if self.rack < 16 else self.rack + 1
        else:
            y = self.rack + 7
        return x, y

    def pickup_coordinates_calculation(self) -> tuple[int, int]:
        if is_odd(self.aisle):
            x = self.coordinates[0] - 1
        else:
            x = self.coordinates[0] + 1
        return x, self.coordinates[1]

    def passage_y_coordinates_calculation(self) -> tuple[int, int]:
        pass
