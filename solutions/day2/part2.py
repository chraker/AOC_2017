from solutions.solution import AbstractSolution


class Part2(AbstractSolution):
    def get_description(self) -> str:
        return "Day 2 part 2: more checksum"

    def run(self) -> int:
        file = open("solutions/day2/input.txt", "r")
        _input = file.read()
        _input = [[int(i) for i in row.split()] for row in _input.splitlines()]
        return self.run_input(_input)

    def run_input(self, custom_input: any) -> int:
        return self.checksum(custom_input)

    def checksum(self, input: list):
        checksum = 0
        for row in input:
            row = sorted(row)
            for c in reversed(row):
                rowCheckSum = None
                for cc in row:
                    if not c % cc and not c is cc:
                        rowCheckSum = c / cc
                        break
                if rowCheckSum is not None:
                    checksum += rowCheckSum
                    break
                row.pop()
        return checksum