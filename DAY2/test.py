import unittest
from DAY2.sol2 import checksum


class TestSolution2(unittest.TestCase):
    def test_sol2(self):
        input = "5 1 9 5 \n 7 5 3 \n 2 4 6 8"
        input = [[int(i) for i in row.split()] for row in input.splitlines() ]
        result = 18
        self.assertEquals(checksum(input), result)

if __name__ == '__main__':
    unittest.main()
