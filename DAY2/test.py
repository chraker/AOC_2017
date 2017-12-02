import unittest

from DAY2.sol2 import *


class TestSolution2(unittest.TestCase):
    def test_sol2part1(self):
        input = "5 1 9 5 \n 7 5 3 \n 2 4 6 8"
        input = [[int(i) for i in row.split()] for row in input.splitlines() ]
        result = 18

        self.assertEquals(checksumP1(input), result)

    def test_sol2part2(self):
        input = "5 9 2 8 \n 9 4 7 3 \n 3 8 6 5"
        input = [[int(i) for i in row.split()] for row in input.splitlines()]
        result = 9

        self.assertEquals(checksumP2(input), result)

if __name__ == '__main__':
    unittest.main()
