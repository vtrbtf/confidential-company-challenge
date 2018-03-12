import itertools
import csv
import urllib.parse

def cargo_permutations(cargos):
    return list(itertools.permutations(range(len(cargos))))

def parse_csv(filename, to_entity):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader, None) #skip headers
        entities = []
        for row in reader:
            entities.append(to_entity(row))
        return entities


def gmaps_parameters(truck, cargo):
    return urllib.parse.urlencode({'api': 1, 'travelmode': 'driving',
                                   'origin': f'{truck.city}, {truck.state}',
                                   'destination': f'{cargo.destination_city}, {cargo.destination_state}',
                                   'waypoints': f'{cargo.origin_city},{cargo.origin_state}'})
