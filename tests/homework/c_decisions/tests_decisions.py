import unittest
from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

class TestConfig(unittest.TestCase):

    def test_get_options_ratio1(self):
        self.assertEqual(0.25, get_options_ratio(5, 20))

    def test_get_options_ratio2(self):
        self.assertEqual(0.5, get_options_ratio(10, 20))

    def test_get_faculty_rating1(self):
        self.assertEqual(get_faculty_rating(0.91), 'Excellent')

    def test_get_faculty_rating2(self):
        self.assertEqual(get_faculty_rating(0.85), 'Very Good')

    def test_get_faculty_rating3(self):
        self.assertEqual(get_faculty_rating(0.71), 'Good')

    def test_get_faculty_rating4(self):
        self.assertEqual(get_faculty_rating(0.66), 'Needs Improvement')

    def test_get_faculty_rating5(self):
        self.assertEqual(get_faculty_rating(0.45), 'Unacceptable')

if __name__ == '__main__':
    unittest.main()
