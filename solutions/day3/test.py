import unittest
from solutions.day3.part1 import Part1


class TestSolution2(unittest.TestCase):
    def test_sol2part1(self):

        p1 = Part1()
        self.assertEquals(p1.run_input(1), 0)
        self.assertEquals(p1.run_input(12), 3)
        self.assertEquals(p1.run_input(23), 2)
        self.assertEquals(p1.run_input(1024), 31)

    def test_sol2part2(self):
        pass

if __name__ == '__main__':
    unittest.main()
