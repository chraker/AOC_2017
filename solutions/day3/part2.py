from enum import Enum

import numpy as np

from solutions.solution import AbstractSolution

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Part2(AbstractSolution):
    def __init__(self):
        self.init()

    def init(self):
        self.spiral = np.ma.zeros((100, 100), dtype=np.int)
        self.origo = [50, 50]
        self.marker = self.origo.copy()

    def get_description(self) -> str:
        return "Day 3: Spiral Memory Stress Test"

    def run(self) -> int:
        file = open("solutions/day3/input.txt", "r")
        _input = file.read()
        return int(self.run_input(int(_input)))

    def run_input(self, custom_input: any) -> int:
        return self.solve(custom_input)

    def solve(self, _input: int):
        self.init() #reset vars
        side = 2
        self.spiral[self.marker[0]][self.marker[1]] = 1
        self.generate(Direction.RIGHT, 1)
        while(self.spiral[self.marker[0]][self.marker[1]] < _input):
            self.generate(Direction.UP, side-1)
            self.generate(Direction.LEFT, side)
            self.generate(Direction.DOWN, side)
            self.generate(Direction.RIGHT, side+1)
            side += 2

        flat_list = [item for sublist in self.spiral for item in sublist]
        flat_list.sort(reverse=True)

        for index, val in enumerate(flat_list):
            if val < _input:
                return flat_list[index-1]


    def generate(self, direction: Direction, steps):
        while steps:
            steps -= 1
            if direction is Direction.UP:
                self.marker[0]-=1
            if direction is Direction.LEFT:
                self.marker[1]-=1
            if direction is Direction.DOWN:
                self.marker[0]+=1
            if direction is Direction.RIGHT:
                self.marker[1]+=1

            self.spiral[self.marker[0]][self.marker[1]] = \
                self.spiral[self.marker[0]-1][self.marker[1]-1] + \
                self.spiral[self.marker[0]-1][self.marker[1]] + \
                self.spiral[self.marker[0]][self.marker[1]-1] + \
                self.spiral[self.marker[0]+1][self.marker[1]-1] + \
                self.spiral[self.marker[0]+1][self.marker[1]+1] + \
                self.spiral[self.marker[0]+1][self.marker[1]] + \
                self.spiral[self.marker[0]][self.marker[1]+1] + \
                self.spiral[self.marker[0]-1][self.marker[1]+1]





