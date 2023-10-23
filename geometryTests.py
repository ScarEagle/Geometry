import unittest
from geometry import Circle, Rectangle

class TestGeometry(unittest.TestCase):

    def test_circle_radius(self):
        self.assertAlmostEqual(Circle.find_circle_radius(12.56637), 2.0, places=2)

    def test_rectangle_area(self):
        self.assertEqual(Rectangle.find_rectangle_area(3, 4), 12)

if __name__ == '__main__':
    unittest.main()
