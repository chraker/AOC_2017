import unittest

from solutions.day4.part1 import Part1
from solutions.day4.part2 import Part2


class TestSolution2(unittest.TestCase):
    def test_sol2part1(self):

        p1 = Part1()
        self.assertTrue(p1.run_input("aa bb cc dd ee"))
        self.assertFalse(p1.run_input("aa bb cc dd aa"))
        self.assertTrue(p1.run_input("aa bb cc dd aaa"))

    def test_sol2part2(self):
        p2 = Part2()
        self.assertTrue(p2.run_input("abcde fghij"))
        self.assertFalse(p2.run_input("abcde xyz ecdab"))
        self.assertTrue(p2.run_input("a ab abc abd abf abj"))
        self.assertTrue(p2.run_input("iiii oiii ooii oooi oooo "))
        self.assertFalse(p2.run_input("oiii ioii iioi iiio"))
        pass

if __name__ == '__main__':
    unittest.main()
