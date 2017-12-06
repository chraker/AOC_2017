from enum import Enum
import collections
import numpy as np
import time

from numpy.core.multiarray import ndarray
from numpy.ma import zeros

from solutions.solution import AbstractSolution


class Part2(AbstractSolution):
    def get_description(self) -> str:
        return "Day 4: High-Entropy Passphrases Part 2"

    def run(self) -> int:
        file = open("solutions/day4/input.txt", "r")
        _input = file.read()
        return self.run_input(_input)

    def run_input(self, custom_input: any) -> int:
        custom_input = [[[ord(letter) for letter in word]
                         for word in row.split()]
                            for row in custom_input.splitlines()]
        return self.solve(custom_input)

    def solve(self, pass_phrases: list):
        return sum(map(self.checkPhrase, pass_phrases))

    def checkPhrase(self, phrase: list) -> bool:
        wordCountSet = set()
        for word in phrase:
            d = self.getWordCountDict(word)
            if d in wordCountSet:
                return False
            else:
                wordCountSet.add(d)
        return True

    def getWordCountDict(self, word):
        s = dict()
        for letter in word:
            if letter in s:
                s[letter] += 1
            else:
                s[letter] = 1
        return frozenset(s.items())
