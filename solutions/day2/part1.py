from solutions.solution import AbstractSolution


class Part1(AbstractSolution):
    def get_description(self) -> str:
        return "Day 2 part 1: checksum"

    def run(self) -> int:
        file = open("solutions/day2/input.txt", "r")
        _input = file.read()
        _input = [[int(i) for i in row.split()] for row in _input.splitlines()]
        return self.run_input(_input)

    def run_input(self, custom_input: any) -> int:
        return self.checksum(custom_input)

    @staticmethod
    def checksum(_input: list):
        checksum = 0
        for row in _input:
            max = min = row[0]
            for c in row:
                if (c > max):
                    max = c
                if (c < min):
                    min = c
            checksum += max - min
        return checksum
