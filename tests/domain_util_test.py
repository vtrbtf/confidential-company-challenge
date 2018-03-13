import unittest
from decimal import Decimal
import math
import domain_util
import domain

class DomainUtilTests(unittest.TestCase):

    def test_create_cargo_permutations(self):
        n = [0, 1, 2, 3, 4]
        p = domain_util.cargo_permutations(n)
        self.assertEqual(len(p), math.factorial(len(n)))
        self.assertEqual(list(p[0]), n)
        self.assertEqual(list(p[-1]), n[::-1])

    def test_parse_csv(self):
        trucks = domain_util.parse_csv("data/trucks.csv", lambda r: domain.Truck(r))
        self.assertEqual(len(trucks), 44)
        self.assertEqual(trucks[0].truck, "Hartford Plastics Incartford")
        self.assertEqual(trucks[0].lat, round(Decimal(34.79981), 5))

    def test_create_google_maps_parameters(self):
        truck = domain.Truck(["TruckMan", "Rio de Janeiro", "RJ", "34.001", "102.11"])
        cargo = domain.Cargo(["Paper", "Vitoria", "ES", "34.001", "102.11", "Sao Paulo", "SP", "20.002", "104.01"])

        self.assertEqual(domain_util.gmaps_parameters(truck, cargo),  "api=1&travelmode=driving&origin=Rio+de+Janeiro%2C+RJ&destination=Sao+Paulo%2C+SP&waypoints=Vitoria%2C+ES")


if __name__ == '__main__':
    unittest.main()
