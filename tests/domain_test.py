import unittest
from decimal import Decimal
import math
import domain_util
import domain

class CargoTests(unittest.TestCase):

    def test_create_cargo(self):
        cargo = domain.Cargo(["Paper", "Vitoria", "ES", "34.001", "102.11", "Sao Paulo", "SP", "20.002", "104.01"])
        self.assertEqual(cargo.product, "Paper")
        self.assertEqual(cargo.origin_city, "Vitoria")
        self.assertEqual(cargo.origin_state, "ES")
        self.assertEqual(cargo.origin_lat, Decimal("34.001"))
        self.assertEqual(cargo.origin_lng, Decimal("102.11"))
        self.assertEqual(cargo.destination_city, "Sao Paulo")
        self.assertEqual(cargo.destination_state, "SP")
        self.assertEqual(cargo.destination_lat, Decimal("20.002"))
        self.assertEqual(cargo.destination_lng, Decimal("104.01"))

    def test_calculate_distance(self):
        cargo = domain.Cargo(["Paper", "Vitoria", "ES", "34.001", "102.11", "Sao Paulo", "SP", "20.002", "104.01"])
        self.assertEqual(round(cargo.origin_dist(Decimal("50.001"), Decimal("60.003")), 6), Decimal(45.044416))


class TruckTests(unittest.TestCase):

    def test_create_truck(self):
        truck = domain.Truck(["TruckMan", "Rio de Janeiro", "RJ", "34.001", "102.11"])
        self.assertEqual(truck.truck, "TruckMan")
        self.assertEqual(truck.city, "Rio de Janeiro")
        self.assertEqual(truck.state, "RJ")
        self.assertEqual(truck.lat, Decimal("34.001"))
        self.assertEqual(truck.lng, Decimal("102.11"))


if __name__ == '__main__':
    unittest.main()
