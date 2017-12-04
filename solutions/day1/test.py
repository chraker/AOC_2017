import unittest

from solutions.day1.part1 import Part1


class TestSolution1(unittest.TestCase):
    def test_sol1(self):
        sequences = [[1, 1, 2, 2], [1, 1, 1, 1], [1, 2, 3, 4], [9, 1, 2, 1, 2, 1, 2, 9]]
        result = [3, 4, 0, 9]

        sol1p1 = Part1()
        self.assertEquals(sol1p1.run_input(sequences[0]), result[0])
        self.assertEquals(sol1p1.run_input(sequences[1]), result[1])
        self.assertEquals(sol1p1.run_input(sequences[2]), result[2])
        self.assertEquals(sol1p1.run_input(sequences[3]), result[3])


if __name__ == '__main__':
    unittest.main()
