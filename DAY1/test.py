import unittest

import time

from DAY1.sol1 import sumSequence


class TestSolution1(unittest.TestCase):
    def test_sol1(self):
        sequences = [[1,1,2,2],[1,1,1,1],[1,2,3,4],[9,1,2,1,2,1,2,9]]
        result = [3,4,0,9]
        self.assertEquals(sumSequence(sequences[0]), result[0])
        self.assertEquals(sumSequence(sequences[1]), result[1])
        self.assertEquals(sumSequence(sequences[2]), result[2])
        self.assertEquals(sumSequence(sequences[3]), result[3])

if __name__ == '__main__':
    unittest.main()
