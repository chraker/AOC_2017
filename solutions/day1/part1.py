from solutions.solution import AbstractSolution


class Part1(AbstractSolution):
    def get_description(self) -> str:
        return "Day 1 part 1: sum sequence"

    def run(self):
        file = open("solutions/day1/input.txt", "r")
        _input = file.read()
        _input = [int(i) for i in _input]
        return str(self.sum_sequence(_input))

    def run_input(self, custom_input: list) -> int:
        return self.sum_sequence(custom_input)

    @staticmethod
    def sum_sequence(sequence: list):
        prev = sequence.pop(0)
        sequence.append(prev)
        sum = 0
        for n in sequence:
            if n is prev:
                sum += n
            prev = n
        return sum
