from distance_picking import distance_picking
from shelf import Shelf


def find_next_location(locations: list[Shelf], start_loc: Shelf = None):
    """
    Поиск ближайшей точки сбора от текущей точки.
    Если передано значение None в качестве текущей точки, то берутся условные стартовые координаты.
    """
    if start_loc is not None:
        list_dist = [
            distance_picking(
                loc1=start_loc.pickup_coordinates,
                loc2=i_location.pickup_coordinates,
                y_low=max((start_loc.upper_passage_y_coordinate, i_location.upper_passage_y_coordinate)),
                y_high=min((start_loc.lower_passage_y_coordinate, i_location.lower_passage_y_coordinate)),
            )
            for i_location in locations
        ]
    else:
        list_dist = [
            distance_picking(
                loc1=(0, 0),
                loc2=i_location.pickup_coordinates,
                y_low=i_location.upper_passage_y_coordinate,
                y_high=i_location.lower_passage_y_coordinate,
            )
            for i_location in locations
        ]
    distance_next = min(list_dist)
    index_min = list_dist.index(min(list_dist))
    next_loc = locations[index_min]
    locations.pop(index_min)
    return start_loc, next_loc, distance_next


with open('input.txt', 'r') as file:
    locations_str = file.read()
locations_list = [Shelf(location) for location in locations_str.split(sep='\n')]
current_location = None
route = []
total_distance = 0
while locations_list:
    start_location, next_location, distance = find_next_location(locations=locations_list, start_loc=current_location)
    current_location = next_location
    total_distance += distance
    route.append(current_location.address)
print(f'Маршрут записан в файл output.txt, дистанция маршрута: {total_distance} ед.')
with open('output.txt', 'w') as file:
    file.write('\n'.join(route))
