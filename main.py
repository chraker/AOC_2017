import time

import solutions.day1.part1 as solDay1P1
import solutions.day1.part2 as solDay1P2
import solutions.day2.part1 as solDay2P1
import solutions.day2.part2 as solDay2P2
from solutions.solution import AbstractSolution


def main():
    run_verbose(solDay1P1.Part1())
    run_verbose(solDay1P2.Part2())
    run_verbose(solDay2P1.Part1())
    run_verbose(solDay2P2.Part2())


def run_verbose(sol: AbstractSolution):
    sTime = time.time()
    print(sol.get_description(), ": Result: ", sol.run(), ", Benchmark: ", time.time() - sTime)


if __name__ == "__main__": main()
