import unittest
from solutions.day2.part1 import Part1
from solutions.day2.part2 import Part2


class TestSolution2(unittest.TestCase):
    def test_sol2part1(self):
        input = "5 1 9 5 \n 7 5 3 \n 2 4 6 8"
        input = [[int(i) for i in row.split()] for row in input.splitlines() ]
        result = 18

        p1 = Part1()
        self.assertEquals(p1.run_input(input), result)

    def test_sol2part2(self):
        input = "5 9 2 8 \n 9 4 7 3 \n 3 8 6 5"
        input = [[int(i) for i in row.split()] for row in input.splitlines()]
        result = 9

        p2 = Part2()
        self.assertEquals(p2.run_input(input), result)

if __name__ == '__main__':
    unittest.main()
