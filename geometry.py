import unittest
import math

def find_circle_radius(area):
    return math.sqrt(area / math.pi)

def find_rectangle_area(length, width):
    return length * width

class TestGeometry(unittest.TestCase):

    def test_circle_radius(self):
        self.assertAlmostEqual(find_circle_radius(12.56637), 2.0, places=2)

    def test_rectangle_area(self):
        self.assertEqual(find_rectangle_area(3, 4), 12)

if __name__ == '__main__':
    unittest.main()
