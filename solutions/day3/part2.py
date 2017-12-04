from solutions.solution import AbstractSolution


class Part2(AbstractSolution):
    def get_description(self) -> str:
        return "Day 2 part 2: more checksum"

    def run(self) -> int:
        file = open("solutions/day2/input.txt", "r")
        _input = file.read()
        return self.run_input(int(_input))

    def run_input(self, custom_input: any) -> int:
        return self.solve(custom_input)

    def solve(self, input: list):
        return 0