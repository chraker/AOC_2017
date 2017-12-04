import unittest

from solutions.day1.part1 import Part1
from solutions.day1.part2 import Part2


class TestSolution1(unittest.TestCase):
    def test_sol1p1(self):
        sequences = [[1, 1, 2, 2], [1, 1, 1, 1], [1, 2, 3, 4], [9, 1, 2, 1, 2, 1, 2, 9]]
        result = [3, 4, 0, 9]

        sol = Part1()
        self.assertEquals(sol.run_input(sequences[0]), result[0])
        self.assertEquals(sol.run_input(sequences[1]), result[1])
        self.assertEquals(sol.run_input(sequences[2]), result[2])
        self.assertEquals(sol.run_input(sequences[3]), result[3])


    def test_sol1p2(self):
        sequences = [[1, 2, 1, 2], [1, 2, 2, 1], [1, 2, 3, 4, 2, 5], [1, 2, 3, 1, 2, 3], [1, 2, 1, 3, 1, 4, 1, 5]]
        result = [6, 0, 4, 12, 4]

        sol = Part2()
        self.assertEquals(sol.run_input(sequences[0]), result[0])
        self.assertEquals(sol.run_input(sequences[1]), result[1])
        self.assertEquals(sol.run_input(sequences[2]), result[2])
        self.assertEquals(sol.run_input(sequences[3]), result[3])
        self.assertEquals(sol.run_input(sequences[4]), result[4])


if __name__ == '__main__':
    unittest.main()
