import unittest
from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Die()
    
    def test_roll_values(self):
        num_rolls = 3
        valid_values = range(1, 6)
        
        for _ in range(num_rolls):
            self.die.roll()
            roll_value = self.die.get_rolled_value()
            self.assertIn(roll_value, valid_values, "The value is out of range")

if __name__ == '__main__':
    unittest.main()
