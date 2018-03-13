import unittest
from decimal import Decimal
import domain_util
import domain
import main

class MainTests(unittest.TestCase):

    def setUp(self):
        self.cargos = domain_util.parse_csv("./data/cargo.csv", lambda r: domain.Cargo(r))
        self.trucks = domain_util.parse_csv("./data/trucks.csv", lambda r: domain.Truck(r))

    def test_create_cargo_truck_distance_index(self):
        index = main.create_cargo_truck_distance_index(self.cargos, self.trucks)
        self.assertEqual(len(index), len(self.cargos))
        self.assertEqual(len(index[0]), len(self.trucks))

        for c in range(len(self.cargos)):
            for t in range(len(self.trucks)):
                self.assertEqual(index[c][t], self.cargos[c].origin_dist(self.trucks[t].lat, self.trucks[t].lng))

    def test_find_nearest_truck_that_was_not_used(self):
        sample_truck_distance_row = main.create_cargo_truck_distance_index(self.cargos, self.trucks)[0]
        sample_truck_distance_row[4] = Decimal(0.0001)
        (index, distance) = main.find_nearest_truck_that_was_not_used(sample_truck_distance_row, set())

        self.assertEqual(index, 4)
        self.assertEqual(distance, Decimal(0.0001))

    def test_raise_error_when_trucks_used_set_is_full(self):
        sample_truck_distance_row = main.create_cargo_truck_distance_index(self.cargos, self.trucks)[0][:4]

        with self.assertRaises(ValueError) as cm:
            (index, distance) = main.find_nearest_truck_that_was_not_used(sample_truck_distance_row, set(range(4)))
            self.assertEqual(cm.exception, "There are no trucks left")

    def test_create_optimal_truck_set_based_on_cargo_order(self):
        index = [[Decimal(10), Decimal(20), Decimal(1)],
                 [Decimal(33), Decimal(40), Decimal(4)],
                 [Decimal(50), Decimal(49.5), Decimal(51)]]

        self.assertEqual(main.create_optimal_truck_set_based_on_cargo_order(index, [0, 1, 2]), [(2, Decimal(1)), (0, Decimal(33)), (1, Decimal(49.5))] )
        self.assertEqual(main.create_optimal_truck_set_based_on_cargo_order(index, [1, 0, 2]), [(0, Decimal(10)), (2, Decimal(4)), (1, Decimal(49.5))] )
        self.assertEqual(main.create_optimal_truck_set_based_on_cargo_order(index, [2, 1, 0]), [(0, Decimal(10)), (2, Decimal(4)), (1, Decimal(49.5))] )


    def test_select_best_cargo_and_truck_permutation(self):
        index = [[Decimal(10), Decimal(20), Decimal(6)],
                 [Decimal(6), Decimal(40), Decimal(4)],
                 [Decimal(50), Decimal(30), Decimal(11)]]

        self.assertEqual(main.select_best_cargo_and_truck_permutation(index, range(3)), ((2, 1, 0), [(1, Decimal('20')), (0, Decimal('6')), (2, Decimal('11'))]))

if __name__ == '__main__':
    unittest.main()
