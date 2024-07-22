import unittest
from src.homework.i_dictionaries_sets.dictionary import get_p_distance, get_p_distance_matrix
class TestConfig(unittest.TestCase):

    def test_p_distance(self):
   
        list1 = ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        list2 = ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
        expected_distance = 0.4
        self.assertAlmostEqual(get_p_distance(list1, list2), expected_distance, places=4)

    def test_get_p_distance_matrix(self):
        
        dna_sequences = [
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
            ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],
            ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        ]
        expected_matrix = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        result_matrix = get_p_distance_matrix(dna_sequences)
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                self.assertAlmostEqual(result_matrix[i][j], expected_matrix[i][j], places=4)

if __name__ == '__main__':
    unittest.main()
