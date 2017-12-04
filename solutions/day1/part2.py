from solutions.solution import AbstractSolution


class Part2(AbstractSolution):
    def get_description(self) -> str:
        return "Day 1 part 2: more sum sequence"

    def run(self):
        file = open("solutions/day1/input.txt", "r")
        _input = file.read()
        _input = [int(i) for i in _input]
        return str(self.sum_sequence(_input))

    def run_input(self, custom_input: list) -> int:
        return self.sum_sequence(custom_input)

    @staticmethod
    def sum_sequence(sequence: list):
        hLength = int(len(sequence)/2)
        sum = 0
        for index, element in enumerate(sequence):
            next = index + hLength
            if next > len(sequence)-1:
                next = next - len(sequence)
            if element is (sequence[next]):
                sum += element
        return sum