import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):



 def test_get_options_ratio1(self):
               self.assert(.25, get_options_ratio(5, 20))
 def test_get_options_ratio2(self):
               self.assert(.5, get_options_ratio(10, 20))

  def test_get_faculty_rating1(self):
               self.assert(get_faculty_rating(.91), 'Excellent')
 def test_get_faculty_rating2(self):
             self.assert(get_faculty_rating(.85), 'Very Good')
 def test_get_faculty_rating3(self):
             self.assert(get_faculty_rating(.71), 'Good')
 def test_get_faculty_rating4(self):
              self.assert(get_faculty_rating(.66), 'Needs Improvement')
 def test_get_faculty_rating5(self):
        self.assert(get_faculty_rating(.45), 'Unacceptable')
#
