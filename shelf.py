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
        pass

    def pickup_coordinates_calculation(self) -> tuple[int, int]:
        pass

    def passage_y_coordinates_calculation(self) -> tuple[int, int]:
        pass
