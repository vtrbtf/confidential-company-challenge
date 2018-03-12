from decimal import Decimal
import domain
import domain_util as util

def create_cargo_truck_distance_index(cargos, trucks):
    index = [None] * len(cargos)
    for i in range(len(cargos)):
        for j in range(len(trucks)):
            distance = cargos[i].origin_dist(trucks[j].lat, trucks[j].lng)
            if index[i] is None:
                index[i] = [distance]
            else:
                index[i].append(distance)
    return index

def find_nearest_truck_that_was_not_used(trucks_row, trucks_used):
    minimum_distance = Decimal('Inf')
    minimum_distance_truck_index = -1
    for truck_index in range(len(trucks_row)):
        if trucks_row[truck_index] < minimum_distance and truck_index not in trucks_used:
            minimum_distance_truck_index = truck_index
            minimum_distance = trucks_row[truck_index]

    if minimum_distance_truck_index == -1:
        raise ValueError("There are no trucks left")

    return (minimum_distance_truck_index, minimum_distance)

def create_optimal_truck_set_based_on_cargo_order(index, cargo_order):
    truck_set = [None] * len(cargo_order)
    trucks_used = set()
    for i in cargo_order:
        (truck_index, distance) = find_nearest_truck_that_was_not_used(index[i], trucks_used)
        truck_set[i] = (truck_index, distance)
        trucks_used.add(truck_index)
    return truck_set

def select_best_cargo_and_truck_permutation(index, cargos):
    best_truck_set = None
    best_cargo_order = None
    min_total_distance = Decimal('Inf')
    for order in util.cargo_permutations(cargos):
        truck_set = create_optimal_truck_set_based_on_cargo_order(index, order)
        total_distance = sum(map(lambda truck_tuple: truck_tuple[1], truck_set))
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            best_truck_set = truck_set
            best_cargo_order = order

    return (best_cargo_order, best_truck_set)


cargos = util.parse_csv("./data/cargo.csv", lambda row: domain.Cargo(row))
trucks = util.parse_csv("./data/trucks.csv", lambda row: domain.Truck(row))
(best_cargo_order, best_truck_set) = select_best_cargo_and_truck_permutation(create_cargo_truck_distance_index(cargos, trucks), cargos)

for cargo_index in best_cargo_order:
    selected_cargo = cargos[cargo_index]
    selected_truck = trucks[best_truck_set[cargo_index][0]]
    url_parameters = util.gmaps_parameters(selected_truck, selected_cargo)

    print(f'- Cargo {selected_cargo.product} will be picked up by Truck {selected_truck.truck}')
    print(f'-- Route: https://www.google.com/maps/dir/?{url_parameters}')
    print(f'---       Truck will be leaving {selected_truck.city},{selected_truck.state}, ')
    print(f'---       picking up the cargo at {selected_cargo.origin_city},{selected_cargo.origin_state} and ')
    print(f'---       delivering it at {selected_cargo.destination_city},{selected_cargo.destination_state}')

    if cargo_index != best_cargo_order[len(best_cargo_order) - 1]:
        print('=' * 64)
        print(' ')

