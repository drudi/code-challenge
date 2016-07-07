# _*_ coding: utf-8 _*_
import unittest
from unittest.mock import patch, MagicMock
from spotippos.models.properties import Properties

class TestProperties(unittest.TestCase):
    def setUp(self):
        self.properties = Properties()

    def tearDown(self):
        del(self.properties)

    def testOne(self):
        self.assertEqual(1, 1, "One equals one")

    def test_point_in_Jaby_province(self):
        provinces = self.properties.get_provinces((1200, 800))
        self.assertEqual(provinces, ["Jaby"], "Wrong province")

    def test_point_in_Gode_and_Ruja(self):
        provinces = self.properties.get_provinces((500, 700))
        self.assertTrue("Gode" in provinces, "Gode should be in the list")
        self.assertTrue("Ruja" in provinces, "Ruja should be in the list")

    def test_get_provinces_with_point_out_of_limits(self):
        provinces = self.properties.get_provinces((-1, -1))
        self.assertEqual(provinces, [], "No provinces should be returned")

    def test_add_new_property(self):
        prop = Properties()
        prop._properties = {'totalProperties' : 0, 'properties' : []}

        prop.add_property(
                {
                    "x": 932,
                    "y": 104,
                    "beds": 5,
                    "baths": 4,
                    "squareMeters": 146
                    })
        self.assertEqual(len(prop._properties['properties']), 1, "Wrong number in list")
        self.assertEqual(prop._properties['totalProperties'], 1, "Wrong total")

    def test_search_prop_in_area(self):
        prop = Properties()
        prop._properties = {'totalProperties' : 2,
                'properties' : [
                    {
                        "id": 1,
                        "x": 500,
                        "y": 500,
                        "beds": 3,
                        "baths": 1,
                        "squareMeters": 60
                        },
                    {
                        "id": 2,
                        "x": 600,
                        "y": 600,
                        "beds": 2,
                        "baths": 1,
                        "squareMeters": 78
                        }
                    ]
                }
        self.assertEqual(
                len(prop.search_prop_in_area((400, 700), (700, 400))['properties']),
                2,
                "Found unexpected number of properties")
        self.assertEqual(
                len(prop.search_prop_in_area((499, 501), (501, 499))['properties']),
                1,
                "Found more properties than expected")

    def test_get_prop_by_id(self):
        prop = Properties()
        prop._properties = {'totalProperties' : 2,
                'properties' : [
                    {
                        "id": 1,
                        "x": 500,
                        "y": 500,
                        "beds": 3,
                        "baths": 1,
                        "squareMeters": 60
                        },
                    {
                        "id": 2,
                        "x": 600,
                        "y": 600,
                        "beds": 2,
                        "baths": 1,
                        "squareMeters": 78
                        }
                    ]
                }
        found = prop.get_property_by_id(1)
        self.assertEqual(found['id'],
                1,
                "Wrong property returned")
        self.assertEqual(set(found['provinces']),
                {'Gode', 'Ruja', 'Scavy'},
                "Wrong provinces in returned property")


if __name__ == "__main__":
    unittest.main()
