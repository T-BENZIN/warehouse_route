def distance_picking(loc1: tuple[int, int], loc2: tuple[int, int], y_low: int, y_high: int) -> int:
    """
    Функция подсчитывающая расстояние между двумя стеллажами на складе.
    Из двух возможных маршрутов выбирается кратчайший.
    Источник: https://medium.com/data-science/optimizing-warehouse-operations-with-python-part-1-83d02d001845
    """
    x1, y1 = loc1[0], loc1[1]
    x2, y2 = loc2[0], loc2[1]
    distance_x = abs(x2 - x1)
    if x1 == x2:
        distance_y1 = abs(y2 - y1)
        distance_y2 = distance_y1
    else:
        distance_y1 = (y_high - y1) + (y_high - y2)
        distance_y2 = (y1 - y_low) + (y2 - y_low)
    distance_y = min(distance_y1, distance_y2)
    distance = distance_x * 30 + distance_y
    return distance


if __name__ == '__main__':
    test_distance = distance_picking((1, 21), (13, 19), 0, 28)
    print(f'Расстояние между 1/A/20 и 8/G/12: {test_distance} ед.')
