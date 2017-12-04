from solutions.solution import AbstractSolution


class Part1(AbstractSolution):
    def get_description(self) -> str:
        return "Day 3: Spiral Memory part1"

    def run(self) -> int:
        file = open("solutions/day3/input.txt", "r")
        _input = file.read()
        return self.run_input(int(_input))

    def run_input(self, custom_input: any) -> int:
        return self.solve(custom_input)

    @staticmethod
    def solve(_input: int):

        generated = 1
        layer = 1

        # get the "layer" or spiral we are on
        while generated < _input:
            layer+=1
            generated=pow(layer+layer-1, 2)

        # max distance is a corner, each step from a corner is -1 steps for the manhattan distance
        # hence we look for closest corner
        side_length = layer+layer-2
        corners = [generated, generated - side_length, generated - side_length*2,
                   generated - side_length*3]
        min_corner_dist = generated

        for corner in corners:
            if abs(_input - corner) < min_corner_dist:
                min_corner_dist = abs(_input - corner)

        return layer + layer - min_corner_dist -2
