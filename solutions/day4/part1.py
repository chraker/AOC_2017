from solutions.solution import AbstractSolution


class Part1(AbstractSolution):
    def get_description(self) -> str:
        return "Day 4: High-Entropy Passphrases Part 1"

    def run(self) -> int:
        file = open("solutions/day4/input.txt", "r")
        _input = file.read()
        return self.run_input(_input)

    def run_input(self, custom_input: any) -> int:
        custom_input = [[str(s) for s in row.split()] for row in custom_input.splitlines()]
        return self.solve(custom_input)

    def solve(self, pass_phrases: list):
        phrases = 0
        for phrase in pass_phrases:
            if(self.checkPhrase(phrase)):
                phrases += 1
        return phrases

    def checkPhrase(self, phrase: list) -> bool:
        words = {}
        for word in phrase:
            if word in words:
                return False
            else:
                words[word]=True
        return True